import os

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.cors import CORSMiddleware

from format_failed_exception import FormattingFailedError
from formatter import CppFormatter, PythonFormatter
from response import ResponseModel

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:8000',
    'https://atcoder.jp'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)


@app.get('/ping')
def ping():
    return {'ping': 'pong'}


@app.post('/format', response_model=ResponseModel)
async def format_code(lang: str, request: Request):
    input_source = (await request.body()).decode('UTF-8')

    try:
        if lang == 'cpp':
            result = CppFormatter.format(input_source)
        elif lang == 'py':
            result = PythonFormatter.format(input_source)
        else:
            raise HTTPException(status_code=400, detail='Unsupported Language')
        return ResponseModel(
            status="ok",
            result=result
        )

    except FormattingFailedError as e:
        return ResponseModel(
            status="error",
            error=e.error
        )


if __name__ == '__main__':
    port = os.getenv('PORT', 9000)
    uvicorn.run(app, host='0.0.0.0', port=port)
