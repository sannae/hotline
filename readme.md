# hotline

### Manually use me

Manually build me: `docker build -t hotline .`

Manually run me: `docker run --name hotline -p 8000:8000 -d hotline`

Troubleshoot if port forward is not working: `docker logs hotline`

### To do

- [ ] tests/test-models.py
- [ ] tests/test-views.py
- [ ] .github/workflows/deploy.yml