### Backend

> _Assumption is that you working under ubuntu and have set up python3.8_

```shell
cd backend

# Install virtual environment
python3.8 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
flask run --reload
```

### Frontend

> _Assumption is that you already installed Node 12+_

```shell
cd frontend

# Install dependencies
npm install

# Run
npm start
```
