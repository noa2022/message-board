import React, { useState } from 'react'

const styles = {
  card: {
    margin: '20px',
    padding: '20px 20px 5px 20px',
    backgroundColor: '#ffffff',
    borderRadius: '10px',
  },
  cardContainer: {
    display: 'flex',
    alignItems: 'center',
  },
  displayName: { fontWeight: 'bold', marginTop: '0px', marginRight: '10px' },
  dateTime: { color: '#c0c0c0', margin: '0px auto auto 10px' },
  messageContainer: { margin: '0px auto 5px auto' },
  buttonContainer: { textAlign: 'right' },
  editButton: {
    padding: '5px 10px',
    backgroundColor: '#ffffff',
    border: '1px solid #ffffff',
    color: '#00bfff',
    cursor: 'pointer',
  },
  saveButton: {
    padding: '5px 10px',
    backgroundColor: '#ffffff',
    border: '1px solid #ffffff',
    color: '#ff7373',
    cursor: 'pointer',
  },
  input: {
    width: '250px',
    marginBottom: '5px',
    padding: '5px',
    border: '1px solid #cccccc',
    borderRadius: '3px',
  },
  textarea: {
    width: '100%',
    height: '70px',
    lineHeight: '1',
    border: '1px solid #cccccc',
    borderRadius: '3px',
  },
}

export const Card = ({ posts, updatePost }) => {
  const [editMode, setEditMode] = useState(null)
  const [currentPost, setCurrentPost] = useState({})

  const handleChange = (e) => {
    const { name, value } = e.target
    setCurrentPost((prev) => ({ ...prev, [name]: value }))
  }

  const handleEdit = (id) => {
    setEditMode(id)
    const postToEdit = posts.find((post) => post.id === id)
    setCurrentPost(postToEdit)
  }
  const handleSave = (id) => {
    updatePost(id, currentPost)
    setEditMode(null)
  }

  return (
    <main>
      {posts.map((item) => (
        <section style={styles.card} key={item.id}>
          <div style={styles.cardContainer}>
            {editMode === item.id ? (
              <input
                style={styles.input}
                type='text'
                name='displayName'
                value={currentPost.displayName}
                onChange={handleChange}
              ></input>
            ) : (
              <p style={styles.displayName} name='displayName'>
                {item.displayName}
              </p>
            )}
            <p style={styles.dateTime} name='date'>
              {item.dateTime}
            </p>
          </div>
          {editMode === item.id ? (
            <textarea
              style={styles.textarea}
              name='message'
              value={currentPost.message}
              onChange={handleChange}
            >
              {currentPost}
            </textarea>
          ) : (
            <p style={styles.messageContainer} name='message'>
              {item.message}
            </p>
          )}
          <div style={styles.buttonContainer}>
            {editMode === item.id ? (
              <button
                style={styles.saveButton}
                onClick={() => handleSave(item.id)}
              >
                保存
              </button>
            ) : (
              <button
                style={styles.editButton}
                onClick={() => handleEdit(item.id)}
              >
                編集
              </button>
            )}
          </div>
        </section>
      ))}
    </main>
  )
}
