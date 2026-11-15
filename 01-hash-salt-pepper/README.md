# 01. Hash Function, Salt and Pepper

## 1. Learning Objectives

Understand how hash functions work and how salt and pepper improve password security.

## 2. Topics

- Hash functions
- SHA-256
- One-way properties
- Salt
- Pepper
- Password hashing

## 3. Experiments

- [ ] Experiment 1: Generate a SHA-256 hash.
- [ ] Experiment 2: Compare hash values for different inputs.
- [ ] Experiment 3: Generate different hashes using salt.
- [ ] Experiment 4: Understand pepper.
- [ ] Experiment 5: Implement password hashing with Argon2id.

## 4. Key Findings

To be completed.

## 5. References

- OWASP Password Storage Cheat Sheet
- Python hashlib documentation
- Python secrets documentation

## 6. Key Findings

### Experiment 1: SHA-256

- SHA-256 generates a 256-bit hash value.
- The hexadecimal representation consists of 64 characters.
- A small change in input produces a significantly different hash.
- The same input always generates the same hash value.

### Conclusion

SHA-256 is a one-way hash function.
However, it is not recommended to use SHA-256 alone
for password storage.
