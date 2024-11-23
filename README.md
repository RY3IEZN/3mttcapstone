<!-- @format -->

# Building and Deploying a Serverless Form-Processing App on GCP with Firestore

Serverless computing has transformed the way developers build and deploy applications by abstracting away server management. With serverless, you can focus solely on writing code while the cloud provider handles infrastructure, scaling, and maintenance. This approach not only reduces operational overhead but also ensures you pay only for what you use.

Google Cloud Platform (GCP) offers a robust suite of serverless solutions, including **Cloud Functions**, **Cloud Run**, and **Firestore**. **Cloud Functions** excels in running small, event-driven functions, while **Cloud Run** allows you to deploy containerized applications with serverless benefits. Combined with Firestore, a fully-managed NoSQL database, these tools enable developers to quickly build scalable, efficient, and cost-effective applications.

In this article, we’ll demonstrate how to leverage GCP's serverless capabilities to create a lightweight form-processing application, where user submissions are seamlessly processed and stored in Firestore—without worrying about servers or scaling complexities.

## **Prerequisites**

Before we start, ensure you have the following:

- A Google Cloud account.
- Basic knowledge of Python and HTML.
- The GCP **Cloud SDK** installed locally.
- GCP APIs enabled:
  - **Cloud Functions API**
  - **Firestore API**

---

In this guide, we’ll follow a this order to build the application. First, we’ll set up a Firestore database to store user data. Next, we’ll create and deploy a serverless Cloud Function to handle form submissions and save the data to Firestore. Finally, we’ll implement a simple HTML frontend and serve it locally on port 5500 using Live Server to test the entire workflow.

## **Step 1: Set Up Your GCP Project**

1. **Create a New GCP Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (e.g., `serverless-form-app`).
2. **Enable Required APIs**:
   - Navigate to **APIs & Services** > **Library**.
   - Enable:
     - **Cloud Functions API**
     - **Firestore API**.

---

## **Step 2: Set Up Firestore**

1. In the GCP Console, go to **Firestore**.
   ![alt](/images/gcpfires1.png)
2. Click **Create Database**. Set the name and the desired region

![alt](/images/gcpfires2a.png)

3. Choose **production mode** for real-world applications or **test mode** for development. In this case use test mode and then click create database

![alt](/images/gcpfires2b.png)

Great we now have our Firestore Db ready, Optionally, you can create a collection, but that will automatically be done in function code

---

### Steps to Deploy a Cloud Function via the GCP Console

1. **Open the GCP Console**:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to **Cloud Run Functions** from the side menu or search for "Cloud Functions."

   ![alt](/images/gcpfnc.png)

2. **Create a New Function**:
   When you click create it might prompt you to enable the api's if you havent done so Before

   ![alt](/images/gcpfnc1.png)

   - Click **Create Function**.
   - Provide a name for your function (e.g., `save_user_input`).
   - Select a region for the function deployment.

3. **Set Trigger and Parameters**:

   - Choose **HTTP Trigger** as the trigger type.
   - Check the option to allow unauthenticated invocations (if necessary).

   ![alt](/images/gcpfnc2.png)

4. **Write Your Code in the Editor**:

   - In the code editor, choose your runtime (e.g., Python 3.10).
   - Add your code directly into the inline editor (e.g., `main.py`).
   - Define the entry point (e.g., `save_user_input`).
   - Add your dependencies to the `requirements.txt` file in the GUI.

   ![alt](/images/gcpfnc3.png)

5. **Deploy the Function**:
   - Click **Deploy** and wait for the deployment to complete.
   - Once deployed, note the provided **Trigger URL** for testing and integration.

After its has been deployed, take note of the function URL, the url will be to invoke the function

![alt](/images/gcpfnc4.png)

Now we have both the function and db ready we can just run the frontend locally using liveserver

# Step 3: Test the Application

we will be using liveserver to run our application locally,o pen the HTML file in a browser. Fill out the form and submit it.

![alt](/images/gcpfnc5a.png)

Check the Firestore database to see if the data is saved correctly

![alt](/images/gcpfnc5b.png)

we’ve successfully built and deployed a serverless form-processing application using GCP’s Cloud Run Functions and Firestore. This architecture is highly scalable, cost-effective, and simplifies backend management. With a few tweaks, you can extend this setup to handle more complex workflows or integrate additional services like email notifications or analytics.

Enjoy!!!
