# AWS CI/CD Infrastructure with Terraform & Jenkins

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

> A production-grade DevOps project demonstrating **Infrastructure as Code**, **CI/CD automation**, and **containerized deployment** on AWS.

---

## 🎬 Live Demo (only while ec2 is up and running)

**🌐 Application**: http://34.235.244.5  
**⚙️ Jenkins**: http://34.235.244.5:8080  
**🔌 API Health**: http://34.235.244.5:5000/health

---

## 🚀 Project Overview

An end-to-end automated deployment pipeline that provisions AWS infrastructure, builds Docker containers, and deploys a full-stack application—all triggered by a simple `git push`.

### What Makes This Special?
- **Zero Manual Setup**: Everything automated from infrastructure to deployment
- **30-Second Deployments**: Push code → Auto-deploy in 30 seconds
- **Fully Reproducible**: Destroy and recreate entire stack in 5 minutes
- **Production Practices**: Real-world DevOps workflows and tooling

---

## 🏗️ Architecture
```
┌─────────────┐
│  Developer  │
│  (git push) │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│     GitHub      │  ◄─── Version Control
└────────┬────────┘
         │ (webhook)
         ▼
┌──────────────────────────────────┐
│       AWS EC2 Instance           │
│  ┌────────────────────────────┐  │
│  │  Jenkins CI/CD Pipeline    │  │
│  │  • Checkout Code           │  │
│  │  • Build Docker Images     │  │
│  │  • Deploy Containers       │  │
│  │  • Health Check            │  │
│  └────────────┬───────────────┘  │
│               ▼                   │
│  ┌────────────────────────────┐  │
│  │    Docker Containers       │  │
│  │  ┌──────────────────────┐  │  │
│  │  │ Frontend (Nginx:80)  │  │  │
│  │  └──────────────────────┘  │  │
│  │  ┌──────────────────────┐  │  │
│  │  │ Backend (Flask:5000) │  │  │
│  │  └──────────────────────┘  │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
           │
           ▼
      ┌─────────┐
      │  Users  │
      └─────────┘
```

---

## ⚡ Key Features

| Feature | Description |
|---------|-------------|
| 🏗️ **Infrastructure as Code** | Entire AWS setup defined in Terraform - no manual clicking |
| 🔄 **Automated CI/CD** | Jenkins pipeline triggered automatically on code push |
| 🐳 **Containerization** | Application packaged in Docker for consistency |
| ☁️ **Cloud Native** | Deployed on AWS with proper security and networking |
| 🚀 **Rapid Deployment** | From code commit to production in 30 seconds |
| 💰 **Cost Efficient** | Runs entirely on AWS Free Tier |

---

## 🛠️ Tech Stack

**Infrastructure & DevOps**
- AWS (EC2, Security Groups, Elastic IP, EBS)
- Terraform (Infrastructure as Code)
- Jenkins (CI/CD Automation)
- Docker (Containerization)

**Application**
- Backend: Python Flask REST API
- Frontend: HTML/CSS/JavaScript
- Web Server: Nginx
- Storage: JSON (lightweight persistence)

---

## 📋 Prerequisites

- AWS Account (Free Tier)
- Terraform installed
- AWS CLI configured
- Git & GitHub account
- SSH key pair

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/tarun08-code/aws-cicd-terraform-project.git
cd aws-cicd-terraform-project
```

### 2. Configure AWS
```bash
aws configure
# Enter AWS Access Key ID
# Enter AWS Secret Access Key
# Region: us-east-1
# Output: json
```

### 3. Deploy Infrastructure
```bash
cd terraform
terraform init
terraform apply
# Type 'yes' to confirm
```

**Save the outputs!** You'll get your EC2 IP, Jenkins URL, and App URL.

### 4. Initial Deployment
```bash
# SSH into EC2
ssh -i ~/Devops.pem ec2-user@<YOUR_EC2_IP>

# Clone and deploy
git clone https://github.com/tarun08-code/aws-cicd-terraform-project.git
cd aws-cicd-terraform-project/app/backend
sudo docker build -t task-backend .
sudo docker run -d --name task-backend -p 5000:5000 task-backend
sudo docker run -d --name task-frontend -p 80:80 \
  -v ~/aws-cicd-terraform-project/app/frontend/index.html:/usr/share/nginx/html/index.html \
  nginx:alpine
```

### 5. Setup Auto-Deploy
1. Configure Jenkins webhook trigger
2. Add GitHub webhook pointing to Jenkins
3. Push code → Watch it auto-deploy! 🎉

---

## 📁 Project Structure
```
aws-cicd-terraform-project/
├── terraform/           # Infrastructure as Code
│   ├── main.tf         # AWS resource definitions
│   ├── variables.tf    # Configuration variables
│   └── outputs.tf      # Output values
├── app/
│   ├── backend/        # Flask API
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── frontend/       # Web UI
│   │   └── index.html
│   └── docker-compose.yml
├── jenkins/
│   └── Jenkinsfile     # CI/CD pipeline definition
└── README.md
```

Jenkins Pipeline Success

![alt text](<screenshoots/Screenshot 2026-03-09 200419.png>)

Application Running

![alt text](<screenshoots/Screenshot 2026-03-09 201441.png>)

GitHub Webhook

![alt text](<screenshoots/Screenshot 2026-03-09 201326.png>)

![alt text](<screenshoots/Screenshot 2026-03-09 201415.png>)

Terraform init Output 

![alt text](<screenshoots/Screenshot 2026-03-08 122722.png>)

Refer more at 

[text](screenshoots)

---

## 🔄 CI/CD Pipeline

**Automated Stages:**

1. **Checkout** - Pull latest code from GitHub
2. **Stop Old Containers** - Clean up previous deployment
3. **Build** - Create fresh Docker images
4. **Deploy** - Start new containers
5. **Health Check** - Verify deployment success

**Trigger:** Automatic on `git push` via GitHub webhook

**Duration:** ~30 seconds

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/tasks` | List all tasks |
| POST | `/api/tasks` | Create task |
| DELETE | `/api/tasks/:id` | Delete task |

---

## 💰 Cost Analysis

**100% AWS Free Tier Eligible!**

- EC2 t3.micro: 750 hours/month free
- EBS 10GB: Within 30GB free tier
- Elastic IP: Free when attached
- Data Transfer: 1GB free

**Monthly Cost: $0** (within free tier limits)

---

## 🎓 What I Learned

### Technical Skills
- **Terraform**: Infrastructure as Code, state management
- **Jenkins**: Pipeline configuration, webhook integration
- **Docker**: Containerization, image building, networking
- **AWS**: EC2, security groups, EBS volume management
- **Linux**: System administration, troubleshooting

### DevOps Concepts
- Infrastructure as Code (IaC)
- Continuous Integration/Continuous Deployment (CI/CD)
- Configuration Management
- Automated Testing & Deployment
- Cloud Architecture

### Real-World Problem Solving
- ✅ Jenkins disk space constraints → EBS volume expansion
- ✅ Container networking → Docker bridge networks
- ✅ Security configurations → AWS security groups
- ✅ State management → Terraform remote state

---

## 🔮 Future Enhancements

- [ ] Kubernetes deployment
- [ ] Prometheus + Grafana monitoring
- [ ] PostgreSQL database
- [ ] HTTPS with Let's Encrypt
- [ ] Blue-green deployment
- [ ] Automated testing in pipeline
- [ ] Multi-environment setup (dev/staging/prod)

---

## 🧹 Cleanup

Stop EC2 when not in use:
```bash
aws ec2 stop-instances --instance-ids <INSTANCE_ID>
```

Destroy all resources:
```bash
cd terraform
terraform destroy
```

Recreate anytime:
```bash
terraform apply
```

---

## 📊 Project Metrics

- **Infrastructure Deployment**: 5 minutes
- **Application Deployment**: 30 seconds
- **Lines of Code**: ~150 (Terraform) + ~200 (Application)
- **Docker Containers**: 2
- **AWS Resources**: 3 (EC2, Security Group, EIP)

---

## 🤝 Connect

**Dineshtarun**  
GitHub: [@tarun08-code](https://github.com/tarun08-code)

---

## 🙏 Acknowledgments

Built during my DevOps/cloud learning journey with inspiration from:
- HashiCorp Terraform Documentation
- Jenkins Community Resources
- Docker Best Practices
- AWS Well-Architected Framework

---

**Built with ❤️ by Dineshtarun**