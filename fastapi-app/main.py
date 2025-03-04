from fastapi import FastAPI
from the_solitary_castle_in_the_mirror import characters
from the_solitary_castle_in_the_mirror.__main__ import _main

app = FastAPI()


@app.get("/")
async def main():
    return _main(characters)
