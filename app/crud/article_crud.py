from sqlalchemy.orm import Session
from app.models.article import Article
from sqlalchemy import or_


def get_articles_by_category(db: Session,category: str):
    
    try:
        articles = (
            db.query(Article)
            .filter(Article.category == category)
            .order_by(Article.published_at.desc())
            .limit(20)
            .all()
        )
        return articles
    finally:
        db.close()
        
        
def search_for_news(db:Session,query: str):
    
    articles = (
        db.query(Article)
        .filter(
            or_(
                Article.title.ilike(f"%{query}%"),
                Article.description.ilike(f"%{query}%"),
            )
        )
        .order_by(Article.published_at.desc())
        .limit(20)
        .all()
    )
    return articles
   



def save_article(db: Session, article_data: dict):
    
    existing_article = db.query(Article).filter(Article.url == article_data["url"]).first()
    if existing_article:
        return  
    
    
    article = Article(**article_data)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


