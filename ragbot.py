import chat_functions as cf

class RAG_Bot:
    def __init__(self, vector_db, client, top_n=2):
        self.vector_db = vector_db
        self.client = client
        self.top_n = top_n
        self.prompt_template = """
        你是一个问答机器人。
        你的任务是根据下述给定的已知信息回答用户问题。

        已知信息:
        {context}

        用户问：
        {query}

        如果已知信息不包含用户问题的答案，或者已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。
        请不要输出已知信息中不包含的信息或答案。
        请用中文回答用户问题。
        """

    def build_prompt(self, prompt_template, **kwargs):
        '''将 Prompt 模板赋值'''
        inputs = {}
        for k, v in kwargs.items():
            if isinstance(v, list) and all(isinstance(elem, str) for elem in v):
                val = '\n\n'.join(v)
            else:
                val = v
            inputs[k] = val
        return prompt_template.format(**inputs)
    
    
    def llm_comletion_api(self, prompt, model="gpt-3.5-turbo-1106"):
        '''封装 openai 接口'''
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,  # 模型输出的随机性，0 表示随机性最小
        )
        return response.choices[0].message.content

    def chat(self, user_query, paragraphs):
        # 1. 检索
        search_results = self.vector_db.search(user_query, paragraphs, self.top_n)

        cf.print_search_results(search_results)

        # 2. 构建 Prompt
        prompt = self.build_prompt(
            self.prompt_template, context=search_results, query=user_query)

        # 3. 调用 LLM
        response = self.llm_comletion_api(prompt)
        return response