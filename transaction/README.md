# Challenge

Hello, Developer!

This is the challenge for developers who are participating in our selection process!
We don't believe in perfect solutions, we just need to understand how you approach software problems.

## Description

You've been hired by an electornic payments company to improve the performance of an API that needs to look up a user's balance.

Assume that the current solution is basic and has only one API that read and write transactions that affect the user's balance directly into the database.
The same API calculates the balance of each user and serves for a mobile application.

At each balance inquiry request, the existing solution is aggregating all user transactions to present the balance.
This process is taking several seconds and your mission is to come up with a better solution.

### Data model

Currently, the database contains the following collumns:

- transaction_id (string)
- user_id (string)
- timestamp (int)
- value (double)

When calling endpoint "_/users/<user_id>/balance_", the system queries the above table filtering all transactions for "_<user_id>_" and returns the sum of the _value_ field.

Your mission is to implement an application that calculates the balance in a better way, using the solution above as a basis.

### Requirements

- [ ] Source code of the new service "_GET /user/<user_id>/balance_";
- [ ] Easy startup, without many steps to be able to start the project in any environment (README);
- [ ] Tests;
- [ ] Define a source code standard and explain it in a document along with the project's source code;
- [ ] Continuous Integration pipeline;
- [ ] API Documentation.

**Observation:** do not spend your time with Front-end implementation.

### What will be tested?

1. Workflow created for the project.
2. Commit history;
3. Semantics and detailing of documentation;
4. Code pattern and test semantics.

**Observation:** other tests may arise according to how the experience with the created solution will be.

### How to start development?

- [ ] Fork the repository for your personal account and add the users @guiferpa and @gabrielbg99;
- [ ] Develop the entire solution in your repository;
- [ ] To deliver, create a Pull Request from a branch with your username from github to the main of the original repository.
