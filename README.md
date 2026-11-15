# Hash Function, Salt and Pepper

## 1. Overview

This project documents my learning about password security, hash functions, salt, and pepper.

## 2. Hash Function

A hash function converts input data into a fixed-length hash value.

### Key characteristics
- One-way function
- Fixed-length output
- Same input produces the same output

### Hashing vs Encryption
- Hashing: Designed to be one-way.
- Encryption: Can be reversed using a decryption key.

## 3. Salt

Salt is random data added to a password before hashing.

### Purpose
- Generate different hash values for identical passwords.
- Prevent attackers from efficiently using precomputed hash tables.

Salt does not need to be secret and is generally stored alongside the password hash.

## 4. Pepper

Pepper is a secret value added to the password hashing process.

### Purpose
- Add another layer of protection.
- Make password attacks more difficult if the password database is compromised.

Pepper must be stored separately from the password database.

## 5. Practical Experiments

- [ ] Calculate a SHA-256 hash using Python.
- [ ] Compare hash values with and without salt.
- [ ] Implement password hashing using Argon2id.
- [ ] Understand password verification.

## 6. Key Takeaways

To be completed through practical experiments.

## 7. References

- OWASP Password Storage Cheat Sheet
- Python hashlib documentation
- Python argon2-cffi documentation
