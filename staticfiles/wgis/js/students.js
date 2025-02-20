document.addEventListener('DOMContentLoaded', function() {
    const serviceDetails = {
        'library': {
            title: 'Library Services',
            content: `
                <div class="service-details">
                    <h3>Library Resources</h3>
                    <ul>
                        <li>Over 1 Million Print Books</li>
                        <li>Digital Journal Subscriptions</li>
                        <li>Online Database Access</li>
                        <li>Study Rooms and Quiet Spaces</li>
                        <li>Research Assistance</li>
                    </ul>

                    <h3>Contact Information</h3>
                    <p>Email: 0d_routing_vague@hidmail.org</p>
                    <p>Phone: (555) 123-4568</p>
                    <p>Location: Main Library Building</p>

                    <h3>Hours of Operation</h3>
                    <ul>
                        <li>Monday - Thursday: 7:00 AM - 12:00 AM</li>
                        <li>Friday: 7:00 AM - 10:00 PM</li>
                        <li>Saturday - Sunday: 9:00 AM - 9:00 PM</li>
                    </ul>

                    <h3>Services Offered</h3>
                    <ul>
                        <li>Book Borrowing and Returns</li>
                        <li>Interlibrary Loans</li>
                        <li>Research Consultations</li>
                        <li>Printing and Scanning</li>
                        <li>Digital Resource Access</li>
                    </ul>
                </div>
            `
        },
        'it-support': {
            title: 'IT Support Services',
            content: `
                <div class="service-details">
                    <h3>Available Services</h3>
                    <ul>
                        <li>24/7 Technical Support Helpdesk</li>
                        <li>Computer Lab Access (Building A, B, and C)</li>
                        <li>Software Installation Assistance</li>
                        <li>Network Connectivity Support</li>
                        <li>Student Email Support</li>
                        <li>Learning Management System (LMS) Help</li>
                    </ul>

                    <h3>Contact Information</h3>
                    <p>Email: 0d_routing_vague@hidmail.org</p>
                    <p>Phone: (555) 123-4567</p>
                    <p>Location: Tech Support Center, Building A, Room 101</p>

                    <h3>Hours of Operation</h3>
                    <ul>
                        <li>Monday - Friday: 8:00 AM - 8:00 PM</li>
                        <li>Saturday: 10:00 AM - 4:00 PM</li>
                        <li>Sunday: Closed</li>
                    </ul>

                    <h3>Common Issues We Handle</h3>
                    <ul>
                        <li>Password Reset</li>
                        <li>WiFi Connection Problems</li>
                        <li>Software Licensing</li>
                        <li>Printer Setup</li>
                        <li>Virus/Malware Removal</li>
                    </ul>
                </div>
            `
        },
        'health': {
            title: 'Health Services',
            content: `
                <div class="service-details">
                    <h3>Medical Services</h3>
                    <ul>
                        <li>Primary Care</li>
                        <li>Mental Health Counseling</li>
                        <li>Vaccination Services</li>
                        <li>Health Education</li>
                        <li>Emergency Care</li>
                    </ul>

                    <h3>Contact Information</h3>
                    <p>Emergency: (555) 911</p>
                    <p>Appointments: (555) 123-4569</p>
                    <p>Location: Health Center, Building D</p>

                    <h3>Hours of Operation</h3>
                    <ul>
                        <li>Monday - Friday: 8:00 AM - 6:00 PM</li>
                        <li>Saturday: 9:00 AM - 1:00 PM (Urgent Care Only)</li>
                        <li>Sunday: Closed (Emergency Services Available)</li>
                    </ul>

                    <h3>Available Services</h3>
                    <ul>
                        <li>Physical Examinations</li>
                        <li>Mental Health Support</li>
                        <li>Laboratory Services</li>
                        <li>Prescription Services</li>
                        <li>Health Insurance Support</li>
                    </ul>
                </div>
            `
        },
        'sports': {
            title: 'Sports Facilities',
            content: `
                <div class="service-details">
                    <h3>Available Facilities</h3>
                    <ul>
                        <li>Modern Gymnasium</li>
                        <li>Olympic-Size Swimming Pool</li>
                        <li>Indoor Basketball Courts</li>
                        <li>Tennis Courts</li>
                        <li>Running Track</li>
                    </ul>

                    <h3>Contact Information</h3>
                    <p>Email: 0d_routing_vague@hidmail.org</p>
                    <p>Phone: (555) 123-4570</p>
                    <p>Location: Sports Complex</p>

                    <h3>Hours of Operation</h3>
                    <ul>
                        <li>Monday - Friday: 6:00 AM - 10:00 PM</li>
                        <li>Saturday - Sunday: 8:00 AM - 8:00 PM</li>
                    </ul>

                    <h3>Programs Offered</h3>
                    <ul>
                        <li>Personal Training</li>
                        <li>Group Fitness Classes</li>
                        <li>Intramural Sports</li>
                        <li>Swimming Lessons</li>
                        <li>Sports Equipment Rental</li>
                    </ul>
                </div>
            `
        },
        counseling: {
            title: 'Counseling Services',
            content: `
                <div class="service-details">
                    <h3>Professional Counseling Support</h3>
                    <p>Our counseling services provide confidential support for:</p>
                    <ul>
                        <li>Academic stress and anxiety</li>
                        <li>Personal and emotional challenges</li>
                        <li>Career guidance and decision-making</li>
                        <li>Relationship and family issues</li>
                        <li>Mental health and wellness</li>
                    </ul>
                    
                    <h3>How It Works</h3>
                    <ol>
                        <li>Fill out our initial consultation form</li>
                        <li>Schedule an appointment with our counselors</li>
                        <li>Attend sessions in-person or virtually</li>
                    </ol>
                    
                    <div class="contact-info">
                        <h3>Contact Information</h3>
                        <p><strong>Location:</strong> Student Center, Room 205</p>
                        <p><strong>Phone:</strong> (555) 123-4567</p>
                        <p><strong>Email:</strong> counseling@university.edu</p>
                        <p><strong>Hours:</strong> Monday-Friday, 9:00 AM - 5:00 PM</p>
                    </div>
                    
                    <button class="schedule-btn">Schedule an Appointment</button>
                    
                    <form id="counselingForm" class="service-form" style="display: none;">
                        <h3>Schedule Counseling Session</h3>
                        <div class="form-group">
                            <label for="counseling-name">Full Name</label>
                            <input type="text" id="counseling-name" required>
                        </div>
                        <div class="form-group">
                            <label for="counseling-email">Email</label>
                            <input type="email" id="counseling-email" required>
                        </div>
                        <div class="form-group">
                            <label for="counseling-student-id">Student ID</label>
                            <input type="text" id="counseling-student-id" required>
                        </div>
                        <div class="form-group">
                            <label for="counseling-type">Type of Counseling</label>
                            <select id="counseling-type" required>
                                <option value="">Select type...</option>
                                <option value="academic">Academic</option>
                                <option value="personal">Personal</option>
                                <option value="career">Career</option>
                                <option value="mental-health">Mental Health</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="counseling-date">Preferred Date</label>
                            <input type="date" id="counseling-date" required>
                        </div>
                        <div class="form-group">
                            <label for="counseling-time">Preferred Time</label>
                            <select id="counseling-time" required>
                                <option value="">Select time...</option>
                                <option value="9:00">9:00 AM</option>
                                <option value="10:00">10:00 AM</option>
                                <option value="11:00">11:00 AM</option>
                                <option value="14:00">2:00 PM</option>
                                <option value="15:00">3:00 PM</option>
                                <option value="16:00">4:00 PM</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="counseling-notes">Additional Notes</label>
                            <textarea id="counseling-notes" rows="4"></textarea>
                        </div>
                        <div class="form-buttons">
                            <button type="submit" class="submit-btn">Submit Request</button>
                            <button type="button" class="cancel-btn">Cancel</button>
                        </div>
                    </form>
                </div>
            `
        },
        financial: {
            title: 'Financial Aid Services',
            content: `
                <div class="service-details">
                    <h3>Financial Support Options</h3>
                    <div class="aid-types">
                        <h4>Scholarships</h4>
                        <ul>
                            <li>Merit-based scholarships</li>
                            <li>Need-based scholarships</li>
                            <li>Athletic scholarships</li>
                            <li>Departmental awards</li>
                        </ul>
                        
                        <h4>Grants</h4>
                        <ul>
                            <li>Federal Pell Grants</li>
                            <li>State Grants</li>
                            <li>Institutional Grants</li>
                        </ul>
                        
                        <h4>Student Loans</h4>
                        <ul>
                            <li>Federal Direct Loans</li>
                            <li>Parent PLUS Loans</li>
                            <li>Private Student Loans</li>
                        </ul>
                    </div>
                    
                    <div class="contact-info">
                        <h3>Financial Aid Office</h3>
                        <p><strong>Location:</strong> Administration Building, Room 150</p>
                        <p><strong>Phone:</strong> (555) 123-8900</p>
                        <p><strong>Email:</strong> 0d_routing_vague@hidmail.org</p>
                    </div>
                    
                    <button class="apply-btn">Apply for Aid</button>
                    
                    <form id="financialForm" class="service-form" style="display: none;">
                        <h3>Financial Aid Application</h3>
                        <div class="form-group">
                            <label for="financial-name">Full Name</label>
                            <input type="text" id="financial-name" required>
                        </div>
                        <div class="form-group">
                            <label for="financial-email">Email</label>
                            <input type="email" id="financial-email" required>
                        </div>
                        <div class="form-group">
                            <label for="financial-student-id">Student ID</label>
                            <input type="text" id="financial-student-id" required>
                        </div>
                        <div class="form-group">
                            <label for="financial-aid-type">Aid Type</label>
                            <select id="financial-aid-type" required>
                                <option value="">Select type...</option>
                                <option value="scholarship">Scholarship</option>
                                <option value="grant">Grant</option>
                                <option value="loan">Student Loan</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="financial-year">Academic Year</label>
                            <select id="financial-year" required>
                                <option value="">Select year...</option>
                                <option value="2024">2024-2025</option>
                                <option value="2025">2025-2026</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="financial-income">Annual Household Income</label>
                            <input type="number" id="financial-income" required>
                        </div>
                        <div class="form-group">
                            <label for="financial-documents">Upload Documents</label>
                            <input type="file" id="financial-documents" multiple>
                            <small>Please upload tax returns, income statements, or other relevant documents</small>
                        </div>
                        <div class="form-buttons">
                            <button type="submit" class="submit-btn">Submit Application</button>
                            <button type="button" class="cancel-btn">Cancel</button>
                        </div>
                    </form>
                </div>
            `
        },
        affairs: {
            title: 'Student Affairs',
            content: `
                <div class="service-details">
                    <h3>Student Affairs Services</h3>
                    <div class="services-list">
                        <h4>What We Offer</h4>
                        <ul>
                            <li>Student Organization Support</li>
                            <li>Campus Event Planning</li>
                            <li>Leadership Development</li>
                            <li>Diversity and Inclusion Programs</li>
                            <li>Student Advocacy</li>
                        </ul>
                    </div>
                    
                    <div class="upcoming-events">
                        <h4>Upcoming Events</h4>
                        <ul>
                            <li>Student Leadership Conference - March 15</li>
                            <li>Cultural Awareness Week - April 1-7</li>
                            <li>Spring Festival - May 1</li>
                        </ul>
                    </div>
                    
                    <div class="contact-info">
                        <h3>Contact Us</h3>
                        <p><strong>Location:</strong> Student Center, Room 301</p>
                        <p><strong>Phone:</strong> (555) 123-5678</p>
                        <p><strong>Email:</strong> 0d_routing_vague@hidmail.org</p>
                    </div>
                    
                    <button class="contact-btn">Get in Touch</button>
                    
                    <form id="affairsForm" class="service-form" style="display: none;">
                        <h3>Student Affairs Contact Form</h3>
                        <div class="form-group">
                            <label for="affairs-name">Full Name</label>
                            <input type="text" id="affairs-name" required>
                        </div>
                        <div class="form-group">
                            <label for="affairs-email">Email</label>
                            <input type="email" id="affairs-email" required>
                        </div>
                        <div class="form-group">
                            <label for="affairs-student-id">Student ID</label>
                            <input type="text" id="affairs-student-id" required>
                        </div>
                        <div class="form-group">
                            <label for="affairs-department">Department</label>
                            <select id="affairs-department" required>
                                <option value="">Select department...</option>
                                <option value="student-org">Student Organizations</option>
                                <option value="events">Event Planning</option>
                                <option value="leadership">Leadership Programs</option>
                                <option value="diversity">Diversity & Inclusion</option>
                                <option value="advocacy">Student Advocacy</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="affairs-subject">Subject</label>
                            <input type="text" id="affairs-subject" required>
                        </div>
                        <div class="form-group">
                            <label for="affairs-message">Message</label>
                            <textarea id="affairs-message" rows="4" required></textarea>
                        </div>
                        <div class="form-buttons">
                            <button type="submit" class="submit-btn">Send Message</button>
                            <button type="button" class="cancel-btn">Cancel</button>
                        </div>
                    </form>
                </div>
            `
        }
    };

    const modal = document.getElementById('serviceModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalContent = document.getElementById('modalContent');
    const closeBtn = document.querySelector('.close-modal');

    // Add click event listeners to all service links
    document.querySelectorAll('.service-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const serviceType = this.dataset.service;
            const service = serviceDetails[serviceType];
            
            if (service) {
                modalTitle.textContent = service.title;
                modalContent.innerHTML = service.content;
                modal.style.display = 'block';
            }
        });
    });

    // Add click event listeners to all support buttons
    document.querySelectorAll('.support-btn').forEach(button => {
        button.addEventListener('click', function() {
            const service = this.getAttribute('data-service');
            const details = serviceDetails[service];
            
            if (details) {
                modalTitle.textContent = details.title;
                modalContent.innerHTML = details.content;
                modal.style.display = 'block';
                
                // Add event listeners for action buttons
                const actionButton = modalContent.querySelector('.schedule-btn, .apply-btn, .contact-btn');
                const form = modalContent.querySelector('.service-form');
                const cancelBtn = modalContent.querySelector('.cancel-btn');
                
                if (actionButton && form) {
                    actionButton.addEventListener('click', function() {
                        // Hide the initial content and show the form
                        const initialContent = modalContent.querySelector('.service-details > *:not(form)');
                        initialContent.style.display = 'none';
                        form.style.display = 'block';
                    });
                }
                
                if (cancelBtn) {
                    cancelBtn.addEventListener('click', function() {
                        // Show the initial content and hide the form
                        const initialContent = modalContent.querySelector('.service-details > *:not(form)');
                        initialContent.style.display = 'block';
                        form.style.display = 'none';
                    });
                }
                
                // Add form submission handler
                const serviceForm = modalContent.querySelector('.service-form');
                if (serviceForm) {
                    serviceForm.addEventListener('submit', async function(e) {
                        e.preventDefault();
                        const formData = new FormData(this);
                        const formObject = {};
                        
                        formData.forEach((value, key) => {
                            formObject[key] = value;
                        });

                        let endpoint = '';
                        switch(this.id) {
                            case 'counselingForm':
                                endpoint = '/api/submit-counseling/';
                                break;
                            case 'financialForm':
                                endpoint = '/api/submit-financial-aid/';
                                break;
                            case 'affairsForm':
                                endpoint = '/api/submit-student-affairs/';
                                break;
                        }

                        try {
                            const response = await fetch(endpoint, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                },
                                body: JSON.stringify(formObject)
                            });

                            const result = await response.json();
                            
                            if (result.status === 'success') {
                                alert('Form submitted successfully! We will contact you soon.');
                                modal.style.display = 'none';
                            } else {
                                alert('There was an error submitting the form. Please try again.');
                            }
                        } catch (error) {
                            console.error('Error:', error);
                            alert('There was an error submitting the form. Please try again.');
                        }
                    });
                }
            }
        });
    });

    // Close modal when clicking the close button
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}); 