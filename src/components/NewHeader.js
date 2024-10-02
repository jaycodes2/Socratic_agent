import React, { useState } from 'react';
import GoogleLoginButton from './GoogleLoginButton';
import { FaRegLightbulb } from 'react-icons/fa'; // Correct import for FaRegLightbulb
import { FiSidebar } from 'react-icons/fi'; // Sidebar toggle icon

function NewHeader({ toggleSidebar, isSidebarOpen }) {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    if (!darkMode) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  };

  return (
    <div className={`flex justify-between items-center p-4 shadow-md transition-colors duration-300 ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
      {/* Left side - Sidebar Toggle */}
      <button
        onClick={toggleSidebar}
        className={`text-2xl button-hover ${darkMode ? 'text-white' : 'text-gray-700'} bg-transparent border-none`} // Added button-hover class and removed background
      >
        <FiSidebar />
      </button>

      {/* Center - Chat App Title */}
      <h1 className={`text-xl font-semibold ${darkMode ? 'text-white' : 'text-gray-800'}`}>
        Socratic Teaching Agent
      </h1>

      {/* Right side - Lantern for dark mode toggle and Google login */}
      <div className="flex items-center space-x-4">
        <button
          onClick={toggleDarkMode}
          className={`text-2xl button-hover ${darkMode ? 'text-white' : 'text-gray-700'} bg-transparent border-none`} // Added button-hover class and removed background
        >
          <FaRegLightbulb className={darkMode ? 'text-yellow-500' : ''} />
        </button>
        <GoogleLoginButton />
      </div>
    </div>
  );
}

export default NewHeader;
