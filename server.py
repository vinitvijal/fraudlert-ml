import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = pickle.load(open('model.pkl', 'rb'))

@app.get("/predict")
def read_root(t, p, a, n):
    print(t,p,a,n)
    
    if t == "CASH_OUT":
        t = 1
    elif t == "PAYMENT":
        t = 2
    elif t == "CASH_IN":
        t = 3
    elif t == "TRANSFER":
        t = 4
    elif t == "DEBIT":
        t = 5
        
    prediction = model.predict([[int(t),float(p),float(a),float(n)]])
    res = bool(prediction[0])
    return {"prediction": res}
