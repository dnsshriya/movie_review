from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)  # base to start the app

# Connect to DB
def get_db():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row     
    return conn

# Redirect root URL to /add
@app.route('/')
def home():
    return redirect('/add')

# Add Review Page
@app.route('/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        title = request.form['title']
        name = request.form['name']
        rating = request.form['rating']
        comment = request.form['comment']

        conn = get_db()
        conn.execute("INSERT INTO reviews (movie_title, reviewer_name, rating, comment) VALUES (?, ?, ?, ?)",
                     (title, name, rating, comment))
        conn.commit()
        conn.close()

        return redirect('/reviews')
    return render_template('add_review.html')

# Show All Reviews Page
@app.route('/reviews')
def reviews():
    conn = get_db()
    rows = conn.execute("SELECT * FROM reviews ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('reviews.html', reviews=rows)


@app.route('/delete/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    conn = get_db()
    conn.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    conn.commit()
    conn.close()
    return redirect('/reviews')
@app.route('/edit/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    conn = get_db()

    if request.method == 'POST':
        title = request.form['title']
        name = request.form['name']
        rating = request.form['rating']
        comment = request.form['comment']

        conn.execute('''
            UPDATE reviews
            SET movie_title = ?, reviewer_name = ?, rating = ?, comment = ?
            WHERE id = ?
        ''', (title, name, rating, comment, review_id))
        conn.commit()
        conn.close()
        return redirect('/reviews')

    review = conn.execute("SELECT * FROM reviews WHERE id = ?", (review_id,)).fetchone()
    conn.close()
    return render_template('edit_review.html', review=review)


if __name__ == '__main__':
    app.run(debug=True)
