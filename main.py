from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.route import router


app = FastAPI()

# 💡 Enable CORS  cross-origin resource sharing 

app.add_middleware(

CORSMiddleware,

allow_origins=["*"], # universal acceptance 

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"],

)

  

# 🔗 Route binding

app.include_router(router)

  

# ✅ Render needs something to bind to 0.0.0.0, so add this

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000) # 📡 Use port 10000 or 8080 as per Render
