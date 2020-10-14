CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT, username TEXT,
        scheduleTag TEXT,
        auto_posting_time TIME,
        is_todey BOOLEAN
);
CREATE TABLE organization(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        organization TEXT,
        faculty TEXT,
        studGroup TEXT,
        tag TEXT
);
CREATE TABLE schedule(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        tag TEXT, day TEXT,
        number INTEGER,
        type TEXT,
        startTime TEXT,
        endTime TEXT,
        title TEXT,
        classroom TEXT,
        lecturer TEXT,
);
CREATE TABLE reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        report TEXT,
        date DATETIME
);