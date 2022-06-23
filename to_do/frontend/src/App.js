import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
//        const users = [
//            {
//                "username": "user1",
//                "first_name": "Frodo",
//                "last_name": "Baggins",
//                "email": "frodo@localhost"
//            },
//            {
//                "username": "user2",
//                "first_name": "Samwise",
//                "last_name": "Gamgee",
//                "email": "samwise@localhost"
//            }
//        ]

//
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div class="container">
                <Menu />
                <UserList users={this.state.users} />
                <Footer />
            </div>
       );
    }
}

export default App;

