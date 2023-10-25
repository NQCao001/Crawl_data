import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    url = 'https://www.vlance.vn/viec-lam-freelance/cpath_cac-cong-viec-it-va-lap-trinh'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    jobs = soup.find_all('.job-item')
    print(jobs)
    print(1)
    return {"message": "Hello"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
