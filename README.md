## Project Introduction:
This project is called ChatPDF, as the name suggests, you can throw a PDF file at it and ask some questions, the system will find relevant content in the PDF and generate answers based on it. (requires calling OpenAI's API)
The vector database used in this project is milvus, an open-source vector database that needs to be configured manually.
## Milvus Configuration Steps:
Download and install docker, you can refer to [this post](https://blog.csdn.net/joeyoj/article/details/136427362)
Download the docker-compose.yml file (already downloaded in the repository), the official download address is [official address](https://github.com/milvus-io/milvus/tree/master/deployments/docker/standalone)
cd to the location where the file is located, execute the following command to start the milvus container and its two dependencies
```
docker compose up -d
```
Here is a milvus [tutorial](https://blog.csdn.net/sinat_39620217/article/details/131847096?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-131847096-blog-127841589.235%5Ev43%5Econtrol&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-131847096-blog-127841589.235%5Ev43%5Econtrol&utm_relevant_index=10) for reference
## Project Configuration:
### Step 1: Set up .env
Configure the OPENAI_API_KEY in the .env file of the project to your own
```
OPENAI_API_KEY="sk-******"
```
### Step 2: Install Packages
Execute the following command:
```
pip install -r requirements.txt
```
### Step 4: Run
Replace the pdf file in PDF_file with the pdf file you want to ask questions about (can only handle text version)
Replace user_query in main.py with questions you are interested in
Run the main.py file
#### Example questions for the sample pdf:
* "What is the name of the first large model product launched by Moonshot?"
* "How many people are there in the current Dark Side of the Moon team?"
* "Is Moonshot an open-source model or a closed-source model?"
* "What does Zhilin Yang think is the necessary prerequisite for doing AGI?"





## 项目介绍：

这个项目叫ChatPDF，顾名思义，可以丢给它一个PDF文件然后提一些问题，系统可找到PDF中相关的内容并据此生成回答。（需要调用OpenAI的API）

该项目用到的向量数据库为milvus，这是一个开源的向量数据库，需要自己配置一下。

## Milvus配置步骤：

下载并安装docker，可参考[这篇帖子](https://blog.csdn.net/joeyoj/article/details/136427362)

下载docker-compose.yml文件（仓库里已下好），官网下载地址为[官网地址](https://github.com/milvus-io/milvus/tree/master/deployments/docker/standalone)

cd 到该文件所在位置处，执行下面命令即可启动milvus容器及其两个依赖

```
docker compose up -d
```

一篇milvus[教程](https://blog.csdn.net/sinat_39620217/article/details/131847096?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-131847096-blog-127841589.235%5Ev43%5Econtrol&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-131847096-blog-127841589.235%5Ev43%5Econtrol&utm_relevant_index=10)供参考

## 项目配置：

### 第一步：设置 .env

把项目中的 .env 里面的 OPENAI_API_KEY 配置为自己的

```
OPENAI_API_KEY="sk-******"
```

## 第二步：安装包

执行下面命令：
```
pip install -r requirements.txt
```

## 第四步：运行

将PDF_file中的pdf文件替换成自己想提问的pdf文件（只能处理文字版）

将main.py中的user_query替换成自己感兴趣的问题

运行 main.py 文件

#### 样例pdf下的问题参考：
* "Moonshot推出的首款大模型产品叫什么名字?"
* " 现在月之暗面团队大约多少人？"
* "Moonshot是开源模型还是闭源模型？"
* " 杨植麟认为做AGI的必要前提是什么？"



