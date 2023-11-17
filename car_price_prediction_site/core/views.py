from django.shortcuts import render, redirect
import pandas as pd
import pickle




def document_view(request):
    return render(request, "core/document.html",
                  {"documents":articles})

def contact_view(request):
      return render(request, "core/contact.html")
    
def homeView(request):
    return render(request, "core/home.html")


def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['Name']
        year = request.POST['year']
        km = request.POST.get("km_driven")
        fuel = request.POST['fuel']
        dealer = request.POST['dealer']
        trans = request.POST['trans']
        seats = request.POST['seats']
        rpm = request.POST['rpm']
        mil = request.POST['mil']
        eng = request.POST['eng']
        power = request.POST['power']
        owner = request.POST['owner']
        print('#####################')

        if name != "":
            df = pd.DataFrame(columns=['year','km_driven','fuel',
                                           'seller_type','transmission','seats',
                                           'torque_rpm','mil_kmpl','engine_cc','max_power_new',
                                           'First Owner','Fourth & Above Owner','Second Owner',
                                           'Test Drive Car','Third Owner'])
            Ownership = Helper(owner)
            df2 = {'year': int(year),'km_driven': float(km),'fuel': float(fuel),
                       'seller_type': int(dealer),'transmission': int(trans),'seats': int(seats),
                        'torque_rpm': float(rpm),'mil_kmpl': float(mil),'engine_cc': float(eng),
                       'max_power_new': float(power),'First Owner': Ownership[0],'Fourth & Above Owner':
                        Ownership[1],'Second Owner': Ownership[2],'Test Drive Car': Ownership[3],
                       'Third Owner': Ownership[4]}

            df = df._append(df2, ignore_index=True)
            # load the model from disk
            filename = 'core/CarSelling.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            res = loaded_model.predict(df)
            print(res)
        else:
            return redirect('model-page')
    else:
        pass

    return render(request, "core/index.html", {'response': res})


def Helper(x):
    if x == '1':
        return [1, 0, 0, 0, 0]
    elif x == '2':
        return [0, 0, 1, 0, 0]
    elif x == '3':
        return [0, 0, 0, 0, 1]
    if x == '4':
        return [0, 1, 0, 0, 0]
    if x == '5':
        return [0, 0, 0, 1, 0]


#####################################FOR  DOCUMENTATION #################3

articles = [
    {
        "name": "Name",
        "definition": """
          When we talk about the "name" of a car, we are referring to the specific 
          model or make of the vehicle. The name of a car is typically a unique identifier 
          given by the manufacturer to distinguish it from other models in their lineup.
          Here are a few key points to understand about the name of a car:
          
          Model Name: The model name represents the specific version or variant of a car 
          produced by a manufacturer. It often consists of a combination of letters, numbers, 
          or words chosen by the manufacturer. For example, "Toyota Camry" or "Ford Mustang" are model names.

          Make: The make of a car refers to the brand or manufacturer that produces the vehicle. 
          It represents the company responsible for designing, engineering, and assembling the car.
          Examples of car makes include Toyota, Ford, Honda, BMW, etc.
      
        """
    },
     {
        "name": "Year",
        "definition": """
         When we talk about the "year" of a car, we are referring to the specific model year in which the
         car was manufactured. The year represents the period in which the car was produced and is often used
         to identify and differentiate different versions of the same model.
        """
    },
    {
        "name": "Km driven",
        "definition": """
          It refers to the total distance that the car has traveled in kilometers. 
          It is a measure of the car's usage or mileage.
          The distance driven by a car is typically measured using the car's odometer, 
          which is a device that keeps track of the total distance traveled by the vehicle. 
          The odometer displays the number of kilometers driven by the car since it was first
          manufactured or since the last time the odometer was reset.
        """
    },
     {
        "name": "Fuel",
        "definition": """
        Fuel is the substance that is used to power the car's engine. It is essentially the energy
        source that allows the car to generate power and move.
        
        In most conventional cars, the fuel used is gasoline or petrol. Gasoline is a refined petroleum 
        product that is derived from crude oil. It is a highly flammable liquid that is combustible in the
        car's engine. When the fuel is ignited in the engine's combustion chamber, it creates controlled 
        explosions that generate the power needed to move the car.
        
        There are also alternative fuels available for cars, such as diesel, ethanol, biodiesel, and electricity.
        The choice of fuel depends on the type of engine the car has and the availability of fuel options in a 
        particular region. Each type of fuel has its own advantages and disadvantages in terms of cost, environmental
        impact, and efficiency.
         
        """
    },
      {
        "name": "Seller Type",
        "definition": """
        When we talk about the "seller type" in the context of a car, it refers to
        the category of the entity or individual selling the car. 
        The seller type can provide information about the source and reliability of 
        the car being sold. Here are some common seller types:
        
        1. Private Seller: A private seller is an individual who is selling their own car. 
        This could be someone who no longer needs the car or wants to upgrade to a different 
        vehicle.

        2. Dealership: A dealership is a business that specializes in selling new and used cars.
        They are authorized by car manufacturers to sell their vehicles. Dealerships often offer
        a wide range of cars, financing options, and after-sales services. They may also provide 
        warranties and certified pre-owned vehicles.

        3. Auction House: Some cars are sold through auction houses, where potential buyers bid on the cars.
        Auctions can be held in person or online, and the cars may come from various sources such as private
        individuals, dealerships, or even fleet vehicles.

        4. Car Broker: A car broker is a professional who acts as an intermediary between the buyer and the seller. 
        They help individuals find and purchase cars based on their specific requirements. Car brokers have access 
        to a wide network of sellers and can negotiate deals on behalf of the buyer.

        5. Online Marketplace: With the rise of online platforms, there are now various
        websites and apps that connect buyers and sellers of cars.
          
        """
    },
       {
        "name": "Transmission",
        "definition": """
        Transmission refers to the component that transfers power from the engine to
        the wheels, allowing the car to change speed and direction. The transmission 
        plays a crucial role in controlling the car's movement and optimizing engine 
        performance.
        
        There are two main types of transmissions commonly found in cars:

Manual Transmission: Also known as a "stick shift" or "manual gearbox," this type of
transmission requires the driver to manually shift gears using a clutch pedal and a gear lever.
It consists of a series of gears that can be engaged or disengaged to change the speed and torque 
delivered to the wheels. Manual transmissions provide the driver with more control over gear selection
and are often preferred by car enthusiasts.

Automatic Transmission: An automatic transmission, also known as an "auto gearbox," is a type of
transmission that automatically changes gears without requiring manual intervention from the driver.

        """
    },
        {
        "name": "Owner",
        "definition": """
       "Owner Type" in the context of a car, it refers to the number of individuals 
       or entities who have previously owned the vehicle. The owner type is often 
       categorized as "first owner," "second owner," and so on, depending on the
       number of previous owners. Let's take a closer look at each owner type:
       
       First Owner: The first owner is the individual or entity who initially
       purchased the car from a dealership or another seller.

      Second Owner: The second owner is the individual or entity who acquires 
      the car after the first owner.

      Subsequent Owners: If the car has had more than two previous owners, 
      they are referred to as subsequent owners. For example, a third owner
      would be the individual or entity who acquired the car after the second owner, and so on.
         
        """
    },
         {
        "name": "Mileage",
        "definition": """
        Mileage refers to the total distance that the vehicle has traveled over its lifetime. 
        Mileage is typically measured in miles or kilometers, depending on the country or region.
        
        The mileage of a car is an important factor to consider when evaluating its condition, usage, 
        and potential value. Here are a few key points to understand about mileage:

        Odometer: The mileage of a car is usually displayed on the odometer, which is a device on the 
        dashboard that tracks and displays the total distance traveled by the vehicle. The odometer can 
        provide an accurate reading of the car's mileage.

        High Mileage vs. Low Mileage: Generally, a car with low mileage is considered to have been driven 
        less and may be perceived as having less wear and tear. On the other hand, a car with high mileage
        has been driven more and may have experienced more mechanical stress and potential maintenance needs.
        However, it's important to note that the overall condition of the car, maintenance history, and how the
        car was driven can also impact its condition, regardless of mileage.

        Average Annual Mileage: The average annual mileage of a car can vary depending on factors such as 
        personal usage, commuting distance, and driving habits. In some regions, the average annual mileage 
        is around 10,000 to 15,000 miles (16,000 to 24,000 kilometers). However, this can vary significantly 
        based on individual circumstances.

        Maintenance and Mileage: Regular maintenance is important for cars, regardless of mileage. However,
        higher mileage cars may require more frequent maintenance and potential repairs due to the increased
        wear and tear on various components.

        Resale Value: Mileage can also impact the resale value of a car. Generally, cars with lower mileage 
        tend to have higher resale value, as they are perceived to have more life left in them.
          
        """
    },
          {
        "name": "Engine",
        "definition": """
        It refers to the main component that generates power to propel the vehicle. 
        The engine is essentially the heart of the car, responsible for converting fuel into mechanical energy.
        
        Here are some key points to understand about car engines:

        Types of Engines: There are different types of car engines, including:

        Internal Combustion Engine (ICE): This is the most common type of engine found in cars.
        It burns fuel internally to generate power. ICEs can be further classified into gasoline 
        engines and diesel engines, depending on the type of fuel used.

        Electric Engine: Electric cars use an electric motor powered by batteries to drive the wheels. 
        These engines do not require fuel combustion and produce zero tailpipe emissions.

        Engine Size and Performance: The size of an engine is often measured in terms of its displacement,
        which refers to the total volume swept by all the pistons in the engine's cylinders. Engine size can
        impact the car's performance, including its power output, acceleration, and fuel efficiency.

        Maintenance: Engines require regular maintenance, including oil changes, filter replacements, and periodic
        inspections. Proper maintenance helps ensure the engine's longevity and optimal performance.

        Engine Efficiency: Car manufacturers strive to improve engine efficiency to maximize power output 
        while minimizing fuel consumption and emissions. Technologies such as turbocharging, direct fuel injection,
        and hybrid systems are used to enhance engine efficiency.
                  
        """
    },
           {
        "name": "Max Power",
        "definition": """
        refers to the maximum amount of power that the car's engine can produce.
        Max power represents the rate at which the engine can do work or produce energy. 
        It indicates the engine's ability to generate power and is often associated with the car's performance capabilities.
    
        """
    },
            {
        "name": "Torque",
        "definition": """
        This is the rotational force generated by the engine. Torque is a crucial aspect of a car's performance.
        Torque is essential for a car's acceleration and pulling power. Higher torque enables a car to accelerate
        quickly from a standstill and maintain speed, especially in situations such as overtaking or climbing uphill.
        """
    },
             {
        "name": "Seats",
        "definition": """
        When we talk about "seats" in the context of a car, we are referring to the individual spaces within the vehicle 
        where passengers can sit. Seats are an essential component of a car's interior, providing comfort and safety for occupants.
         
        """
    },
]

