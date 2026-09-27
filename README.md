# ComicCraft

AI Powered Comic Generator using FastAPI and Gemini.

## Install

Create virtual environment:

python -m venv venv

Activate:

venv\Scripts\activate

Install packages:

pip install -r requirements.txt

## Environment

Create a file named:

.env

Add:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

## Start the FASTAPI Server

uvicorn app.main:app --reload

## Website

http://127.0.0.1:8000

## FastAPI Documentation

http://127.0.0.1:8000/docs

## API Endpoints

/generate-comic/json

/generate

/export-success

/test-image

/comic-preview

/health
