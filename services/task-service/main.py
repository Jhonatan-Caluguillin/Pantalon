from fastapi import FastAPI, APIRouter

# 1. Definir el router PRIMERO
router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return {"message": "Lista de tareas"}

# 2. Crear la aplicación
app = FastAPI(title="Task Service")

# 3. Incluir el router DESPUÉS de definirlo
app.include_router(router)

@app.get("/")
def health():
    return {"status": "Task Service running"}