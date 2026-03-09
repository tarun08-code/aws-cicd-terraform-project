# AWS CI/CD Infrastructure with Terraform & Jenkins

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

A production-grade DevOps project demonstrating **Infrastructure as Code (IaC)**, **CI/CD pipeline automation**, and **containerized application deployment** on AWS.

---

## 🚀 Project Overview

This project showcases a complete **DevOps workflow** from infrastructure provisioning to automated deployment:

- **Infrastructure as Code**: Entire AWS infrastructure defined in Terraform
- **Automated Deployment**: Jenkins CI/CD pipeline for continuous deployment
- **Containerization**: Docker & Docker Compose for application packaging
- **Cloud Deployment**: Running on AWS EC2 with proper security configurations

---

## 🏗️ Architecture
```
GitHub Repository
       ↓
   [Push Code]
       ↓
Jenkins Pipeline (EC2)
       ↓
   [Build Docker Images]
       ↓
   [Deploy Containers]
       ↓
Application Running (EC2)
   ├── Frontend (Nginx) - Port 80
   └── Backend (Flask API) - Port 5000
```

---

## 🛠️ Tech Stack

### Infrastructure & DevOps
- **Cloud Provider**: AWS (EC2, VPC, Security Groups, Elastic IP)
- **Infrastructure as Code**: Terraform
- **CI/CD**: Jenkins
- **Containerization**: Docker, Docker Compose

### Application
- **Backend**: Python Flask REST API
- **Frontend**: HTML/CSS/JavaScript (Vanilla)
- **Web Server**: Nginx
- **Data Storage**: JSON file (simple persistence)

---

## ✨ Features

✅ **Fully Automated Infrastructure**
- Terraform provisions entire AWS environment
- Security groups configured for SSH, HTTP, Jenkins
- Elastic IP for consistent public access

✅ **CI/CD Pipeline**
- Automated builds on GitHub push
- Docker image building and deployment
- Health checks and deployment verification

✅ **Containerized Application**
- Backend API in Python Flask
- Frontend served via Nginx
- Isolated, reproducible environments

✅ **Production-Ready Setup**
- Automated installation of Docker, Jenkins, Git
- Proper security group configurations
- Health monitoring endpoints

---

## 📋 Prerequisites

- AWS Account (Free Tier eligible)
- Terraform installed locally
- AWS CLI configured with credentials
- Git & GitHub account
- Basic knowledge of Linux commands

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tarun08-code/aws-cicd-terraform-project.git
cd aws-cicd-terraform-project
```

### 2️⃣ Configure AWS Credentials
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: us-east-1
# Default output: json
```

### 3️⃣ Deploy Infrastructure with Terraform
```bash
cd terraform
terraform init
terraform plan
terraform apply
# Type 'yes' to confirm
```

**Save the outputs!** You'll get:
- `instance_public_ip`: Your EC2 server IP
- `jenkins_url`: Jenkins dashboard URL
- `app_url`: Application URL

### 4️⃣ SSH into EC2 and Deploy Application
```bash
ssh -i ~/Devops.pem ec2-user@<YOUR_EC2_IP>
cd ~
git clone https://github.com/tarun08-code/aws-cicd-terraform-project.git
cd aws-cicd-terraform-project/app/backend
sudo docker build -t task-backend .
sudo docker run -d --name task-backend -p 5000:5000 task-backend
sudo docker run -d --name task-frontend -p 80:80 \
  -v ~/aws-cicd-terraform-project/app/frontend/index.html:/usr/share/nginx/html/index.html \
  nginx:alpine
```

### 5️⃣ Access Your Application

- **Frontend**: http://YOUR_EC2_IP
- **Backend API**: http://YOUR_EC2_IP:5000/health
- **Jenkins**: http://YOUR_EC2_IP:8080

---

## 🔧 Project Structure
```
aws-cicd-terraform-project/
├── terraform/
│   ├── main.tf              # Main infrastructure definition
│   ├── variables.tf         # Input variables
│   └── outputs.tf           # Output values
├── app/
│   ├── backend/
│   │   ├── app.py           # Flask API application
│   │   ├── Dockerfile       # Backend container image
│   │   └── requirements.txt # Python dependencies
│   ├── frontend/
│   │   └── index.html       # Web interface
│   └── docker-compose.yml   # Multi-container orchestration
├── jenkins/
│   └── Jenkinsfile          # CI/CD pipeline definition
└── README.md
```

---

## 📦 Infrastructure Components

### AWS Resources Created by Terraform

| Resource | Purpose |
|----------|---------|
| **EC2 Instance (t3.micro)** | Hosts application & Jenkins |
| **Security Group** | Firewall rules for ports 22, 80, 5000, 8080 |
| **Elastic IP** | Static public IP address |
| **User Data Script** | Auto-installs Docker, Jenkins, Git on boot |

### Resource Tags

All resources are tagged with:
- `Name`: `devops-project-*`
- Easily identifiable in AWS console

---

## 🔄 CI/CD Pipeline Stages

The Jenkins pipeline (`jenkins/Jenkinsfile`) performs:

1. **Checkout**: Pull latest code from GitHub
2. **Stop Old Containers**: Remove running containers
3. **Build Backend**: Create new Docker image
4. **Deploy**: Start fresh containers
5. **Health Check**: Verify application is running

---

## 🌐 API Endpoints

### Backend API (Flask)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/tasks` | Get all tasks |
| POST | `/api/tasks` | Create new task |
| DELETE | `/api/tasks/:id` | Delete task by ID |

---

## 💰 Cost Estimation

**AWS Free Tier Eligible!**

- **EC2 t3.micro**: 750 hours/month free
- **EBS Storage**: 8GB (within 30GB free tier)
- **Elastic IP**: Free when attached to running instance
- **Data Transfer**: 1GB outbound free

**Estimated Monthly Cost**: $0 - $5 (if staying within free tier limits)

---

## 🛡️ Security Features

- SSH access via key pair authentication
- Security group restricts access to necessary ports only
- Jenkins authentication required
- Docker containers run in isolated environments

---

## 🔮 Future Enhancements

- [ ] Add Kubernetes deployment (migrate from Docker)
- [ ] Implement blue-green deployment strategy
- [ ] Add monitoring with Prometheus & Grafana
- [ ] Integrate automated testing in pipeline
- [ ] Add database (PostgreSQL/MySQL) instead of JSON
- [ ] Implement HTTPS with Let's Encrypt
- [ ] Add GitHub webhook for auto-deployment
- [ ] Infrastructure backup automation

---

## 🧹 Cleanup

To avoid AWS charges, destroy all resources:
```bash
cd terraform
terraform destroy
# Type 'yes' to confirm
```

This will delete:
- EC2 instance
- Security group
- Elastic IP
- All associated resources

---

## 📝 What I Learned

- **Infrastructure as Code**: Using Terraform to provision reproducible cloud infrastructure
- **CI/CD Automation**: Building Jenkins pipelines for automated deployments
- **Containerization**: Packaging applications with Docker for consistency
- **Cloud Architecture**: Designing secure, scalable AWS deployments
- **DevOps Workflows**: End-to-end automation from code commit to production

---

## 🤝 Contributing

This is a learning project, but suggestions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📧 Contact

**Dineshtarun**  
GitHub: [@tarun08-code](https://github.com/tarun08-code)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- AWS Free Tier for hosting
- HashiCorp Terraform for IaC
- Jenkins community for CI/CD tools
- Docker for containerization platform

---

**⭐ If this project helped you learn DevOps, please give it a star!**

---

## 🎬 Live Demo

**Application URL**: http://34.235.244.5  
**Jenkins Dashboard**: http://34.235.244.5:8080  

### Features Demonstrated:
- ✅ Automated infrastructure provisioning with Terraform
- ✅ CI/CD pipeline with Jenkins
- ✅ Auto-deployment on GitHub push
- ✅ Containerized application with Docker
- ✅ Full-stack task manager (Flask + Vanilla JS)

---

## 🎓 Key Learnings

### Technical Skills Gained:
1. **Terraform** - Writing infrastructure as code, managing AWS resources
2. **Jenkins** - Building CI/CD pipelines, configuring webhooks
3. **Docker** - Containerizing applications, managing images
4. **AWS** - EC2, Security Groups, EBS volumes, networking
5. **Git/GitHub** - Version control, webhooks, collaboration

### DevOps Concepts Mastered:
- Infrastructure as Code (IaC)
- Continuous Integration/Continuous Deployment (CI/CD)
- Container orchestration
- Cloud infrastructure management
- Automated deployment workflows

### Challenges Overcome:
- Jenkins disk space monitoring issues
- EBS volume expansion
- Docker container networking
- Security group configuration
- Terraform state management

---

## 📊 Project Metrics

- **Lines of Terraform Code**: ~150
- **Docker Containers**: 2 (frontend + backend)
- **AWS Resources Created**: 3 (EC2, Security Group, EIP)
- **Deployment Time**: ~30 seconds (after code push)
- **Infrastructure Deployment Time**: ~5 minutes

---

## 🔄 CI/CD Pipeline Flow
```
Developer Push → GitHub Webhook → Jenkins Trigger
                                         ↓
                                   Checkout Code
                                         ↓
                                  Stop Old Containers
                                         ↓
                                  Build Docker Images
                                         ↓
                                  Deploy New Containers
                                         ↓
                                    Health Check
                                         ↓
                                  ✅ Deployment Complete!
```

---

## 💡 What I Would Add Next

Given more time, I would enhance this project with:

1. **Kubernetes** - Migrate from Docker to K8s for better orchestration
2. **Monitoring** - Add Prometheus + Grafana dashboards
3. **Database** - Replace JSON with PostgreSQL/MySQL
4. **HTTPS** - SSL certificates with Let's Encrypt
5. **Load Balancer** - AWS ALB for high availability
6. **Auto-Scaling** - Dynamic scaling based on traffic
7. **Blue-Green Deployment** - Zero-downtime deployments
8. **Automated Testing** - Unit tests + integration tests in pipeline
9. **Secrets Management** - AWS Secrets Manager integration
10. **Multi-environment** - Dev, Staging, Production setups

---

## 🙏 Acknowledgments

This project was built as part of my DevOps learning journey. Special thanks to the open-source community and the amazing documentation from:
- HashiCorp (Terraform)
- Jenkins Community
- Docker
- AWS

---

**Built with ❤️ by Dineshtarun**

