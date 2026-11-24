CREATE TABLE dormitory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    verification_code TEXT NOT NULL
);

#TODO: to discuss user role as admin or user
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    bio TEXT,
    is_verified BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dormitory_id INTEGER NOT NULL,
    FOREIGN KEY (dormitory_id) REFERENCES dormitory (id)
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    type TEXT NOT NULL CHECK (type IN ('request', 'offer')),
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'done')),
    reward_type TEXT NOT NULL DEFAULT 'none' CHECK (reward_type IN ('none', 'thanks', 'money')),
    reward_note TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL,
    dormitory_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (dormitory_id) REFERENCES dormitory (id),
    FOREIGN KEY (category_id) REFERENCES category (id)

);

CREATE TABLE post_helper (
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (post_id, user_id),
    FOREIGN KEY (post_id) REFERENCES post (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE  
);

CREATE TABLE message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN NOT NULL DEFAULT 0,
    sender_id INTEGER NOT NULL,
    recipient_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES user (id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_id) REFERENCES user (id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES post (id) ON DELETE CASCADE

);