import logo from '../logo.svg';

const Menu = () => {
    return (
        <div class="d-flex justify-content-between" style={{backgroundColor: '#c3d5e7'}}>
            <div class="">
                <a class="nav navbar-brand align-items-center" href="#">
                    <img src={logo} width="50" height="50" alt="" loading="lazy" />TO-DO List
                </a>
            </div>


            <ul class="nav align-items-center">
                <li class="nav-item"><a class="nav-link" href='#'>All users</a></li>
                <li class="nav-item"><a class="nav-link" href='#'>Project</a></li>
                <li class="nav-item"><a class="nav-link" href='#'>TO-DO</a></li>
            </ul>
        </div>
    )
}

export default Menu