from sqlalchemy.orm import Session

from ..models import QuoteBase
from ..schemas import Quote
from uuid import UUID

def get_quote(db: Session, quote_id: UUID):
    return db.query(QuoteBase).filter(QuoteBase.id == quote_id).first()

def get_quotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(QuoteBase).offset(skip).limit(limit).all()

def create_quote(db: Session, quote: Quote):
    db_quote = QuoteBase(author=quote.author, content=quote.content,
            tags=quote.tags, source=quote.source)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)

    return db_quote


