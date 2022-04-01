FROM node:16-alpine

WORKDIR /client

COPY package.json .
COPY package-lock.json .

RUN npm install
RUN npm install react-scripts@5.0.0 -g

COPY . .

CMD ["npm", "run", "start"]
