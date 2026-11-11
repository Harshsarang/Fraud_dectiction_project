from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
#from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates
#from starlette.responses import HTMLResponse
#from pymongo import MongoClient
from schema.user_input import UserInput
from model.predict import predict_output
from schema.prediction_response import PredictionResponse

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="templates")

#conn = MongoClient("mongodb://localhost:27017")

#@app.get("/", response_class=HTMLResponse)
#async def read_item(request: Request):
#    look = list(conn.fd_db.income_data.find({}))
#    for data in look:
#        print(data)

#    for data in look:
#        data["_id"] = str(data["_id"])

#    return templates.TemplateResponse(
#        request,
#        name="item.html",
#        context={'record': look}
#    )



@app.get('/')
def home():
    return {'Message':'Fraud Dectation Transaction Predection'}

@app.get("/health")
async def health_check():
    return ({
        "Status": "Server is connected"
    })

@app.post("/predict", response_model=PredictionResponse)
def predict_fraud(data: UserInput):

    user_input = {
        'amount': data.amount,
        'oldbalanceOrg': data.your_balance_before_transaction,
        'newbalanceOrig': data.your_balance_after_transaction,
        'oldbalanceDest': data.receiver_balance_before_transaction,
        'newbalanceDest': data.receiver_balance_after_transaction,
        'balance_diff': data.balance_difference,
    }

    try:
    #prediction we make from external file so its good practice to have try and except to dectect error easily
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content = prediction)

    except Exception as e:

        return JSONResponse(status_code=500, content={'error': str(e)})



