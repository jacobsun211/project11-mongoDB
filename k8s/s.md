## 1. Rebuild the Docker image with your fix


bash
cd app

# Rebuild with the same tag
docker build -t jacobsun211/contacts-api:v1 .


If you want to version it explicitly (recommended):

bash
docker build -t jacobsun211/contacts-api -t aharonsegal/fastapi:latest .


You do *not* have to delete the old image first; the new build just overwrites the tag locally.

---

## 2. (Optional but smart) Test the image locally

Before pushing, quickly verify that the import error is really gone:

bash
docker run --rm -p 8000:8000 jacobsun211/contacts-api:v1
# or: docker run --rm -p 8000:8000 aharonsegal/fastapi:v1


Then open: http://localhost:8000/docs.

If it runs fine here, you know the image itself is good.