import unicodedata
import re

def remove_invisible_characters(text):
    return ''.join(c for c in text if not unicodedata.category(c).startswith('C'))

def normalize_text(text):
    text = unicodedata.normalize('NFKC', text)  # 半角全角を統一
    text = remove_invisible_characters(text)  # 不可視文字を削除
    text = text.lower()  # 小文字に変換
    text = re.sub(r'[\s\r\n]+', '', text)  # 改行、空白、タブなどを削除
    # 特殊表記を標準化
    text = text.replace('㈱', '株式会社')
    # よくある表記ゆれを統一
    text = re.sub(r'(株式会社|有限会社|合同会社|グループ|一般社団法人|一般財団法人|公益社団法人|公益財団法人|医療法人|学校法人|宗教法人|社会福祉法人|農業協同組合|漁業協同組合|生活協同組合|労働組合|特定非営利活動法人|独立行政法人|地方独立行政法人|特殊法人|特定目的会社|外国法人|㈱｜\（株\）|\(株\))', '', text)
    return text

def has_partial_match(g_name, h_name, length=4, threshold=3):
    if g_name == h_name:
        return True

    for i in range(len(g_name) - length + 1):
        substring = g_name[i:i + length]
        dist = distance(substring, h_name)
        if dist <= threshold:
            return True
    return False

text="㈱トヨタレンタリース愛知"
normalize_text(text)

