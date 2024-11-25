import { useState, useEffect } from 'react';
import axios from 'axios';


const App = () => {
  interface User {
    user_id: string;
  }

  const [userInfo, setUserInfo] = useState<User[]>([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/user/')
      .then(res => {
        setUserInfo(res.data);
      });
  }, []);

  console.log(userInfo);

  return (
    <div>
      <div>
        {userInfo.map(user => <div key={user.user_id}>{user.user_id}</div>)}
      </div>
    </div>
  );
}

export default App;
