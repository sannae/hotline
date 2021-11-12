# hotline

Manually build: `sudo docker build -t my-django-image .`

Manually run: `sudo docker run --name my-django-cont -p 8000:8000 -d my-django-image`

Troubleshoot if port forward not working: `sudo docker logs my-django-cont`

## To do

- [ ] Add project management
- [ ] Add development project management