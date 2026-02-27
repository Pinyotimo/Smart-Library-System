# Smart Library System 📚

## Overview
A Pythonic library management system built without external databases.  
Demonstrates advanced Python features: OOP, dunder methods, decorators, closures, packaging, MRO, and duck typing.

## Features
- **Book & Library classes** with magic methods (`__str__`, `__len__`, `__eq__`, `__getitem__`)
- **Logging decorator** to track borrow/return actions with timestamps
- **Permission closure** for role-based access control
- **Duck typing**: `borrow_item()` works on any object with a `.title` attribute
- **Package structure** for professional organization

## Usage
```bash
cd library_system
python -m library_system