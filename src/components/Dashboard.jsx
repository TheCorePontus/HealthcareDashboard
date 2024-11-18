import React, { useState } from 'react';
import { Upload, User, Save } from 'lucide-react';

const Dashboard = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    file: null
  });

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
    alert('Information submitted successfully!');
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
            <User className="text-blue-500 mr-3" />
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
            <input 
              type="number"
              name="age"
              placeholder="Patient Age"
              value={formData.age}
              onChange={handleInputChange}
              min="0"
              max="120"
              className="w-full focus:outline-none"
              required
            />
          </div>
          
          <div className="border rounded-lg p-2 flex items-center">
            <Upload className="text-blue-500 mr-3" />
            <input 
              type="file"
              name="medicalFile"
              onChange={handleFileUpload}
              className="w-full focus:outline-none"
            />
          </div>
          
          <button 
            type="submit" 
            className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition flex items-center justify-center"
          >
            <Save className="mr-2" /> Submit Patient Information
          </button>
        </form>
      </div>
    </div>
  );
};

export default Dashboard;