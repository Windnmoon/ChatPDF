from openai import OpenAI
from dbconnector import MyVectorDBConnector
import chat_functions as cf
from ragbot import RAG_Bot

# 加载环境变量
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # 读取本地 .env 文件，里面定义了 OPENAI_API_KEY



if __name__ == '__main__':

    client = OpenAI()
    paragraphs = cf.extract_text_from_pdf(
    ".\PDF_file\Moonshot.pdf",
    page_numbers=[0, 1, 2, 3], # 选择要提取的页码，注释该行则为全部PDF页
    min_line_length=5
    )

    # 创建一个向量数据库对象
    print('\n' + '-' * 20 + ' 创建向量数据库对象 ' + '-' * 20 + '\n')
    vector_db = MyVectorDBConnector("milvus_for_ChatPDF", client)

    # 向向量数据库中添加文档
    print('-' * 20 + ' 开始文档灌库 ' + '-' * 20 + '\n')  
    vector_db.add_documents(paragraphs)

    bot = RAG_Bot(vector_db, client, top_n=3)

    user_query1 = "Moonshot推出的首款大模型产品叫什么名字?"
    user_query2 = '现在月之暗面团队大约多少人？'
    user_query3 = 'Moonshot是开源模型还是闭源模型？'
    user_query4 = '杨植麟认为做AGI的必要前提是什么？'

    print('-' * 20 + ' Chatting! ' + '-' * 20 + '\n')
    response = bot.chat(user_query1, paragraphs)

    print(response)

    




    
