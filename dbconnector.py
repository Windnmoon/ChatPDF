from pymilvus import (
  connections,
  FieldSchema,
  CollectionSchema,
  DataType,
  Collection,
)


class MyVectorDBConnector:
    def __init__(self, collection_name, client):
        '''初始化 Milvus 连接器'''
        self.connect = connections.connect("default", host="localhost", port="19530")

        self.fields = [
        FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=1536)
        ]

        self.index = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128},
        }

        self.schema = CollectionSchema(self.fields, "This is a milvus schema for a project named ChatPDF~~~")

        self.collection = Collection(collection_name, self.schema)

        self.client = client

        self.insert_result = None

    def get_embeddings(self, texts, model="text-embedding-ada-002", dimensions=None):
        '''封装 OpenAI 的 Embedding 模型接口'''
        if model == "text-embedding-ada-002":
            dimensions = None
        if dimensions:
            data = self.client.embeddings.create(
                input=texts, model=model, dimensions=dimensions).data
        else:
            data = self.client.embeddings.create(input=texts, model=model).data
        return [x.embedding for x in data]


    def add_documents(self, documents):
        '''灌库：向 collection 中添加文档与向量'''
        entities = [
        # provide the pk field because `auto_id` is set to False
        [str(i) for i in range(len(documents))],  # 每个段落的 id
        self.get_embeddings(documents)  # 每个段落的向量
        ]

        self.insert_result = self.collection.insert(entities)

        self.collection.flush()

        self.collection.create_index("embeddings", self.index)

        self.collection.load()


    def search(self, query, paragraphs, top_n=2):
        '''检索向量数据库'''
        search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
        }

        vectors_to_search = [self.get_embeddings([query])[0]]
        
        search_results = self.collection.search(
        vectors_to_search,
        "embeddings", 
        search_params, 
        limit=top_n, 
        output_fields=["embeddings"]
        )

        hit_para_idxs = search_results[0].ids

        search_results = [paragraphs[int(i)] for i in hit_para_idxs]

        return search_results