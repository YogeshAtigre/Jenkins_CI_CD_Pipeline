Here's a detailed step-by-step guide to set up a **Jenkins CI/CD pipeline for a Flask application**:

---

## **Step 1: Install and Configure Jenkins**
### **1.1 Install Jenkins on a Virtual Machine or Cloud Server**
You can install Jenkins on an **Ubuntu** machine using the following steps:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openjdk-11-jdk -y  # Install Java (Jenkins prerequisite)
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
```
Start and enable Jenkins:
```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

### **1.2 Access Jenkins**
- Open a browser and go to: `http://<your-server-ip>:8080`
- Retrieve the initial admin password:
  ```bash
  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
  ```
- Follow the on-screen instructions to complete the setup.

### **1.3 Install Necessary Jenkins Plugins**
- Navigate to **Manage Jenkins > Plugins** and install:
  - **Pipeline**
  - **Git**
  - **GitHub Integration**
  - **Email Extension**

---

## **Step 2: Configure Jenkins with Python**
### **2.1 Install Python and Dependencies**
Ensure Python 3 and pip are installed on your Jenkins server:
```bash
sudo apt install python3 python3-pip -y
python3 --version  # Verify installation
```
### **2.2 Install Virtual Environment and Flask**
```bash
pip3 install virtualenv flask pytest
```
### **2.3 Install Git**
```bash
sudo apt install git -y
```

---

## **Step 3: Fork and Clone the Flask Application**
### **3.1 Fork the Sample Repository**
Use a sample repository for a Flask web application, e.g.:
- **Sample Flask App Repo:** [https://github.com/YogeshAtigre/Jenkins_CI_CD_Pipeline.git]

- Click **Fork** on GitHub and copy the URL of your forked repository.

### **3.2 Clone the Repository in Jenkins Server**
```bash
git clone https://github.com/<your-github-username>/<reponame>.git
cd flask-app
```

---

## **Step 4: Create a Jenkins Pipeline**
### **4.1 Create a Jenkinsfile**
Inside your Flask app repository, create a `Jenkinsfile` (sample code shared in the repo)
---

## **Step 5: Configure Jenkins Pipeline Job**
### **5.1 Create a New Jenkins Pipeline Job**
1. Go to **Jenkins Dashboard > New Item**.
2. Select **Pipeline** and provide a name eg: **Flask-CI-CD**.
3. Under **Pipeline Definition**, select **Pipeline script from SCM**.
4. Choose **Git** and enter your **repository URL**.
5. In **Branch Specifier**, enter `main`.
6. Click **Save**.

---

## **Step 6: Configure Automatic Triggers**
1. Open **Flask-CI-CD Job** in Jenkins.
2. Click **Configure > Build Triggers**.
3. Select **Poll SCM** and enter:
   ```
   H/5 * * * *  (Runs every 5 minutes)
   ```
   OR
   Select **GitHub Webhook** to trigger builds on push.

---

## **Step 7: Set Up Email Notifications**
1. Go to **Manage Jenkins > Configure System**.
2. Scroll to **E-mail Notification**:
   - Set SMTP Server to: `smtp.gmail.com`
   - Use port `587`
   - Enable **Use SMTP Authentication**
   - Enter Gmail credentials (Use an App Password if needed).
   - Test and save settings.

---

## Jenkinsfile Overview:
- **Build**: Install dependencies.
- **Test**: Run unit tests.
- **Deploy**: Deploy to a staging environment.
---

## **Step 8: Run and Verify the Pipeline**
1. Go to **Jenkins Dashboard**.
2. Select **Your Provided Job name eg:Flask-CI-CD Job**.
3. Click **Build Now**.
4. Monitor **Console Output** for success/failure logs.


---

### **Conclusion**
Following these steps, you have successfully set up a **CI/CD pipeline for a Flask application using Jenkins**. The pipeline automates **code checkout, dependency installation, testing, and deployment**. 🚀
