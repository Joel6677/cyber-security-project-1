# CYBER SECURITY BASE PROJECT 1

LINK TO THE REPOSITORY: https://github.com/Joel6677/cybersecurity-project-1

How to set up the application:

1. Run the following commands:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
   - `python manage.py runserver`
2. To fix the flaws you might need to run the following:
   - `pip install django-axes`
   - `pip install python-decouple`

Flaws:

### FLAW 1: Broken Access Control

- **Exact Source Link:** [Flaw 1 Source](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll/views.py#L78)
- **Description of Flaw 1:** Users must not have the ability to exceed their designated permissions. Failures in access control could result in potential vulnerabilities, including unauthorized data disclosure, alteration, data loss, or the execution of business functions beyond the user’s authorized scope. Currently there are no proper authorization checks for deleting polls. Users can delete other user’s polls by first creating a poll, inspecting the delete button and then manipulating the form action to target a specific poll for deletion.

- **How to Fix Flaw 1:** This flaw can be fixed by modifying the `views.py` file's `delete_poll` method. Firstly, we need to enable Django’s built-in login system to ensure user authentication. Next, the check whether the current user is the same as the creator of the poll must be added.
- **Links to Fixes for Flaw 1:**
   - [Fix 1](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll/views.py#L77)
   - [Fix 2](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll/views.py#L84)

### FLAW 2: Cryptographic Failures

- **Exact Source Link:** [Flaw 2 Source](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L26)
- **Description of Flaw 2:** Sensitive information, such as passwords, should be protected in the application. Cryptographic failures refer to cases where cryptographic systems or protocols designed to protect sensitive information or secure communication are compromised by problems or vulnerabilities that undermine their effectiveness. In the `settings.py` file, `SECRET_KEY` must be hidden in production. Exposing the `SECRET_KEY` could lead to various security risks, such as the compromise of session management and data encryption.
- **How to Fix Flaw 2:** It is important to securely hide and protect this value in the production environment. This could be done, for example, by storing it in an `.env` file. To achieve this, we could import `config` from `python-decouple` and set `SECRET_KEY = config('SECRET_KEY')`. To do that, we must first install it by `pip install python-decouple` and then create an `.env` file where we store the `SECRET_KEY` value. Finally, we import `decouple` in the `settings.py` file and set the `SECRET_KEY` to `config('SECRET_KEY')`. It must be noted that the `.env` file should be hidden and added to the `.gitignore` file, but as demonstrative purposes, I haven't done that. If you haven't already installed `python-decouple` in your system, run `pip install python-decouple`.
- **Links to Fixes for Flaw 2:**
   - [`.env` File](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/.env#L1)
   - [Settings.py](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L27)

### FLAW 3: Security Misconfiguration

- **Exact Source Link:** [Flaw 3 Source](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L30)
- **Description of Flaw 3:** The application should be configured in a way that doesn’t make it vulnerable to security threats and attacks. Security misconfiguration is often caused when security best practices are not followed during the configuration process, or default settings are left unchanged, and the application is left unintentionally for security weaknesses. In this project, a security misconfiguration flaw is present due to enabling Django’s debug mode. Enabling debug in the production environment has the potential to expose critical information to malicious actors. For example, it could expose sensitive configuration details and stack traces, which could be used for attacks or exploitation.
- **How to Fix Flaw 3:** To fix this flaw, one must set `DEBUG` to `False` in the production environment. Also, the `ALLOWED_HOSTS` must be placed. For this project, I have set the `ALLOWED_HOSTS` variable to `[‘*’]` for illustrative purposes. In a real-world deployment scenario, this should be replaced with a list of trusted hostnames or IP addresses for enhanced security.
- **Link to Fix for Flaw 3:**
   - [Settings.py](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L31)

### FLAW 4: Identification and Authentication Failures

- **Exact Source Link:** [Flaw 4 Source](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L169)
- **Description of Flaw 4:** It is critical that the user’s identity, authentication, and session management should be protected against authentication-related attacks. Currently, the application allows users to make unlimited login attempts without any restrictions. This could lead the application vulnerable to brute force attacks.
- **How to Fix Flaw 4:** This flaw could be fixed, for example, by incorporating Django-axes in the project. Django-axes provides mechanisms for limiting login attempts. This will significantly enhance the security of the identification and authentication processes, minimizing the risk of unauthorized access due to brute force attacks. If you haven't already installed Django-axes, install it by running `pip install django-axes`.
- **Link to Fix for Flaw 4:**
   - [Settings.py](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L170)

### FLAW 5: Security Logging and Monitoring Failures

- **Exact Source Link:** [Flaw 5 Source](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L117)
- **Description of Flaw 5:** Logging and monitoring is critical in order to help detect, escalate, and respond to active breaches.
The absence of a logging and monitoring system in the application could lead the significant security concerns since it hinders the application’s capability to monitor crucial security events. This could lead to undetected security incidents and vulnerabilities.
- **How to Fix Flaw 4:** In my project this flaw could be addressed by using the Django’s built-in logging system. 
- **Link to Fix for Flaw 5:**
   - [Fix 1](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll_project/settings.py#L117)
   - [Fix 2](https://github.com/Joel6677/cyber-security-project-1/blob/67f58a29b6de9523219f5de1b359408a541fdab6/poll/views.py#L9)
