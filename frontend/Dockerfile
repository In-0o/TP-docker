FROM nginx:alpine
# A COMPLETER
EXPOSE 80
ENV TZ="Europe/Paris"
COPY . /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]