from fastapi import FastAPI, File, UploadFile
from fastapi import Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Depends,status ,responses,Response
import pandas as pd
from utils import ProcessKeywords
from middleware import sizemiddleware

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# app.add_middleware(sizemiddleware)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

# size_middleware=sizemiddleware(app)


@app.post("/upload/")
async def upload_csv(myfile: UploadFile = File(...)):
    try:
      # csvReader = csv.DictReader(codecs.iterdecode(myfile.file, 'utf-8'))
        df = pd.read_csv(myfile.file)
        df.fillna('')
        if len(df)> 100:
           return {"Status":"Uploading error", "message":"100 keywords can process at once  " }
        else:
          keywords_set = df[['Keyword','Search volume']]
          process_keywords = ProcessKeywords(keywords_set=keywords_set, pivot =4)
          process_keywords.process_keywords()  
          return FileResponse("output.csv")
      
    except Exception as e:
      return {"status": "error", "message": str(e)}

      # print(csvfile)
      # # process_keywords.
      # with open('csvfile.csv','w') as f:requests           2.28.2 lume']
      #   csvWriter=csv.DictWriter(f,fieldnames=fieldnames)
      #   csvWriter.writeheader()
      #   for row in csvReader:
      #    new_row={"keywords_names":row["Keyword"],
      #             "Volume":row["Volume"]}
      #    csvWriter.writerow(new_row)