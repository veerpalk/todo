-- create User Table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username varchar(255) NOT NULL,
  password varchar(255) NOT NULL
) 

-- create tasks table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending',
    user_id INT NOT NULL,
    priority ENUM('High', 'Medium', 'Low') NOT NULL DEFAULT 'High',
    created_date datetime DEFAULT CURRENT_DATE(),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

--Alter tasks table
ALTER TABLE tasks
ADD COLUMN due_date DATETIME DEFAULT (CURRENT_DATE() + INTERVAL 1 DAY),
ADD COLUMN category ENUM('Work', 'Home', 'Self', 'Family', 'Study') DEFAULT 'Work';
     




-- Sample Data  for users

INSERT INTO users (username, password) VALUES
( 'veer', '$2b$12$dtYE2piJeGLP.88/cartkOJ3813bEm1GfARFaYq1WClZO/dlxDnpy'),
('rohan', '$2b$12$Q9MCxSE1xiRfM07s4v/eHONQrcMg/Yap.jFuFduInaPHO1Bm8/xZ2'),
( 'tashu', '$2b$12$5KlAKmm4QmLRsVpDki6sJegt0YEJNXDi/fgF8Un87aqkzTmsJ3DFy'),
( 'preet', '$2b$12$ma9ibDhfZp0KjNYzkn4Tt.IA8PsmL4datL/5onRKOF.cEEqfMLLly'),
( 'kartik', '$2b$12$lK5U9GWpsr8znl6uYr.GoOVfjtZA948wRtsoCcKw0DDpUs3InkByK');


-- Sample Data  for Task
INSERT INTO tasks ( title, description, status, user_id, priority, created_date, due_date, category) VALUES
( 'Plan Trip', 'Plan trip to Finland', 'Completed', 2, 'Low', '2023-07-03 17:13:27', '2023-07-05 00:00:00', 'Work'),
( 'Go for Shopping', 'Buy Dress and Official outfit', 'Pending', 2, 'High', '2023-07-03 17:13:27', '2023-07-05 00:00:00', 'Work'),
( 'Hit Gym', 'Do Cardio and weight lifting', 'In Progress', 3, 'Medium', '2023-07-03 17:13:27', '2023-07-05 00:00:00', 'Work'),
( 'Drink Water', 'Drink 4-5 L of water', 'Pending', 4, 'High', '2023-07-03 00:00:00', '2023-07-05 00:00:00', 'Work'),
( 'Apply G ', 'Go to DriveTest centre', 'Completed', 1, 'Medium', '2023-07-04 00:00:00', '2023-07-05 00:00:00', 'Work'),
( 'Watch Netflix', 'Watch Death Note on Netflix', 'Completed', 1, 'Medium', '2023-07-04 00:00:00', '2023-07-05 00:00:00', 'Work'),
( 'Go for Shopping', 'Buy new clothes , have some suits as well', 'In Progress', 6, 'Medium', '2023-07-04 00:00:00', '2023-07-05 00:00:00', 'Work'),
( 'Study', 'Study Maths', 'Pending', 6, 'High', '2023-07-04 00:00:00', '2023-07-05 00:00:00', 'Work'),
(12, 'Do Gardening', 'Grow some flowers and plants', 'Completed', 6, 'Low', '2023-07-04 00:00:00', '2023-07-05 00:00:00', 'Work'),
(14, 'ITR ', 'Fill ITR', 'Completed', 1, 'High', '2023-07-04 00:00:00', '2023-07-04 18:00:00', 'Work'),
(15, 'Play Games', 'Play Cricket', 'In Progress', 1, 'Medium', '2023-07-04 00:00:00', '2023-07-05 14:28:00', 'Home'),
(17, 'Watch Movie', 'Watch RRR', 'In Progress', 1, 'Low', '2023-07-04 00:00:00', '2023-07-05 03:32:00', 'Work');








