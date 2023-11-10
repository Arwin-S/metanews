# Use an official Node runtime as a parent image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Build the app (for production you might want to use `npm run build` instead)
# RUN npm run build

# Expose the port the app runs on
EXPOSE 5173

# Define the command to run your app using CMD which defines your runtime
CMD ["npm", "run", "dev"]
