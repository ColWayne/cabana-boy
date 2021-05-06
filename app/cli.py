import secrets
from app import app, db
from app.models import Token


@app.cli.command("create-token")
def create_token():
    generated_token = secrets.token_urlsafe(32)
    token = Token(key=generated_token)
    db.session.add(token)
    db.session.commit()
    print(generated_token)
    return


@app.cli.command("revoke-tokens")
def revoke_tokens():
    all_tokens = Token.query.all()
    for t in all_tokens:
        db.session.delete(t)
    db.session.commit()
