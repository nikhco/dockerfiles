FROM node:alpine

ARG username=username
ARG secret=secret

RUN apk add git
RUN git clone https://github.com/feedbin/extract.git /app

WORKDIR /app
RUN npm install

RUN mkdir users
RUN echo "$secret" > users/$username

CMD ["node","app/server.js"]