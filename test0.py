import re

# 假设这是你的输入字符串
userWord = "a cheap mexican restaurant"
meanOfUser = "inform(pricerange=cheap,food=mexican,type=restaurant)"

# 使用正则表达式找到所有的键值对
pattern = re.compile(r'(\w+)=(\w+)')
matches = pattern.findall(meanOfUser)

# 创建一个字典来存储键值对，方便查找
attributes = {key: value for key, value in matches}

# 对 userWord 进行分词处理
words = userWord.split()

# 对每个词进行检查和替换
formatted_words = []
for word in words:
    # 找到当前词对应的 key
    key = next((k for k, v in attributes.items() if v == word), None)
    if key:
        # 如果找到了对应的 key，按照指定格式替换
        formatted_words.append(f"[{word}]({key})")
    else:
        # 如果没有找到，保持原样
        formatted_words.append(word)

# 将处理后的词重新组合成字符串
formatted_userWord = ' '.join(formatted_words)
print(formatted_userWord)