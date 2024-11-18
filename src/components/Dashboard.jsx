import React, { useState } from 'react';

const Dashboard = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    file: null
  });

  
  const ageOptions = Array.from({length: 101}, (_, i) => i);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    setFormData(prev => ({
      ...prev,
      file: file
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!formData.name || !formData.age) {
      alert('Please fill in all required fields');
      return;
    }

    console.log('Submitted Data:', formData);
    alert('Patient information submitted successfully!');
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-md">
        <div className="text-center mb-6">
          <h1 className="text-2xl font-bold text-blue-600">Dashboard</h1> <br />
          <p className="text-gray-500">Patient Information Submission</p>
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="flex items-center border rounded-lg p-2">
            <span className="text-blue-500 mr-3">👤</span>
            <input 
              type="text"
              name="name"
              placeholder="Patient Name"
              value={formData.name}
              onChange={handleInputChange}
              className="w-full focus:outline-none"
              required
            />
          </div>
          
          <div className="flex items-center border rounded-lg p-2">
            <span className="text-blue-500 mr-3">🎂</span>
            <select
              name="age"
              value={formData.age}
              onChange={handleInputChange}
              className="w-full focus:outline-none"
              required
            >
              <option value="">Select Age</option>
              {ageOptions.map(age => (
                <option key={age} value={age}>
                  {age}
                </option>
              ))}
            </select>
          </div>
          
          <div className="border rounded-lg p-2 flex items-center">
            <span className="text-blue-500 mr-3">📄</span>
            <input 
              type="file"
              name="medicalFile"
              onChange={handleFileUpload}
              className="w-full focus:outline-none"
            />
          </div>
          
          <button 
            type="submit" 
            className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
          >
            Submit Patient Information
          </button>
        </form>
      </div>
    </div>
  );
};

export default Dashboard;
