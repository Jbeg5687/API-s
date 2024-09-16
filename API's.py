const express = require('express');
const app = express();
app.use(express.json());

let books = [];
let nextId = 1;

// Add a new book
app.post('/api/books', (req, res) => {
    const { bookName, author, publisher } = req.body;
    if (!bookName || !author || !publisher) {
        return res.status(400).json({ message: 'Missing fields' });
    }
    const book = { id: nextId++, bookName, author, publisher };
    books.push(book);
    res.status(201).json(book);
});

// Get all books
app.get('/api/books', (req, res) => {
    res.status(200).json(books);
});

// Get a book by ID
app.get('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id == req.params.id);
    if (!book) {
        return res.status(404).json({ message: 'Book not found' });
    }
    res.status(200).json(book);
});

// Update a book by ID
app.put('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id == req.params.id);
    if (!book) {
        return res.status(404).json({ message: 'Book not found' });
    }
    const { bookName, author, publisher } = req.body;
    if (bookName) book.bookName = bookName;
    if (author) book.author = author;
    if (publisher) book.publisher = publisher;
    res.status(200).json(book);
});

// Delete a book by ID
app.delete('/api/books/:id', (req, res) => {
    const index = books.findIndex(b => b.id == req.params.id);
    if (index === -1) {
        return res.status(404).json({ message: 'Book not found' });
    }
    books.splice(index, 1);
    res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(Server running on port ${PORT});
});