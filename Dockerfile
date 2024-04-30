FROM node:18-alpine
COPY ./ app
RUN python app/tests/test_bot.py