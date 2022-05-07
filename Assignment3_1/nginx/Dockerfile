# create image based on NGINX image
FROM nginx

# remove the defalt configuration file
RUN rm /etc/nginx/conf.d/default.conf

# copy the file as the new configuration
COPY nginx.conf /etc/nginx/conf.d/
