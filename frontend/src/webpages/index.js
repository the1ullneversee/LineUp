import React from 'react';
import {
  Switch,
  Route,
  Link,
  BrowserRouter,
  Routes,
  Router
} from "react-router-dom";

import Home from './home';
import User from './user';
import DC from '../data_connector'
const Webpages = () => {
    return(
      <div>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<DC />} />
            <Route path="/user/:id" element={<User />} />
          </Routes>
        </BrowserRouter>
      </div>
    );
};
export default Webpages;