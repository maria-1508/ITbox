from app import app
from models import db, Vocabulary

data =[
    {"word_jp": "サーバー", "word": "server", "meaning": "Máy chủ"},
    {"word_jp": "クライアント", "word": "client", "meaning": "Khách hàng"},
    {"word_jp": "データベース", "word": "database", "meaning": "Cơ sở dữ liệu"},
    {"word_jp": "ネットワーク", "word": "network", "meaning": "Mạng"},
    {"word_jp": "セキュリティ", "word": "security", "meaning": "Bảo mật"},
    {"word_jp": "プログラミング", "word": "programming", "meaning": "Lập trình"},
    {"word_jp": "アルゴリズム", "word": "algorithm", "meaning": "Thuật toán"},
    {"word_jp": "ソフトウェア", "word": "software", "meaning": "Phần mềm"},
    {"word_jp": "ハードウェア", "word": "hardware", "meaning": "Phần cứng"},
    {"word_jp": "クラウドコンピューティング", "word": "cloud computing", "meaning": "Điện toán đám mây"}
]

with app.app_context():
    for item in data:
        vocabulary = Vocabulary(word_jp=item["word_jp"], word=item["word"], meaning=item["meaning"])
        db.session.add(vocabulary)
    db.session.commit()
    print("data ok")