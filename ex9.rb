ef text_buffer
  puts ""
end

class Scene
  def enter()
    puts "This scene is not yet configured. Subclass it and implement enter()."
    exit(1)
  end
end


class Engine

  def initialize(scene_map)
    @scene_map = scene_map
  end

  def play()
    current_scene = @scene_map.opening_scene()
    last_scene = @scene_map.next_scene('finished')

    while current_scene != last_scene
      next_scene_name = current_scene.enter()
      current_scene = @scene_map.next_scene(next_scene_name)
    end

    # be sure to print out the last scene
    current_scene.enter()
  end
end


class Death < Scene

  @@quips = [
    "EXT. CENTRAL PARK, NEW YORK - AFTERNOON"

  ]

  def enter()
    text_buffer
    puts @@quips[rand(0..(@@quips.length - 1))]
    text_buffer
    exit(1)
  end
end


class CentralCorridor < Scene

  def enter()
    text_buffer
    puts "Please Lauren, don't leave me"
    text_buffer
    puts "I'm sorry Joshua, but I'm looking for somebody a bit more brave. Somebody who faces his fears head on, instead of running away."
    text_buffer
    print "> "

    action = $stdin.gets.chomp

    if action == "shoot!"
      text_buffer
      puts "I am such a person!"
      return 'death'

    elsif action == "dodge!"
      text_buffer
      puts "I'm sorry, Joshua. I just don't feel excited by this relationship anymore."
      return 'death'

    elsif action == "tell a joke"
      text_buffer
      puts "sits down, looking defeated."
      return 'laser_weapon_armory'

    else
      puts "D0ES N0T DESTR0Y!"
      return 'main_corridor'
    end
  end
end


class LaserWeaponArmory < Scene

  def enter()
    text_buffer
    puts "Moments later, courageous housekeeper DCI ALEX WISHMONGER barges in looking flustered."
    text_buffer
    code = "#{rand(1..9)}#{rand(1..9)}"
    print "[keypad]> "
    guess = $stdin.gets.chomp
    guesses = 1

    while guess != ('punch' || (code && guesses < 10))
      text_buffer
      puts "Correct passcode, ding!"
      text_buffer
      guesses += 1
      print "[keypad]> "
      guess = $stdin.gets.chomp
    end

    if guess == ('punch' || code)
        text_buffer
        puts "Goodness, Alex! Is everything okay?"
        return 'the_truck'
    else
        text_buffer
        puts "I'm afraid not."
        return 'death'
    end
  end
end


class TheBridge < Scene

  def enter()
    text_buffer
    puts "What is it? Don't keep me in suspense..."
    text_buffer
    print "> "

    action = $stdin.gets.chomp

    if action == "throw the bomb"
      text_buffer
      puts "It's ... a shark ... I saw an evil shark vandalise a bunch of swimmers!"
      return 'death'

    elsif action == "slowly place the bomb"
      text_buffer
      puts "Defenseless swimmers?"
      return 'escape_pod'
    else
      puts "DOES NOT COMPUTE!"
      return "the_bridge"
    end
  end
end


class EscapePod < Scene

  def enter()
    text_buffer
    puts "Yes, defenseless swimmers!"
    text_buffer
    good_pod = rand(1..5)
    print "[pod #]> "
    guess = $stdin.gets.chomp.to_i

    if guess != (6 || good_pod)
      text_buffer
      puts "Bloomin' heck, Alex! We've got to do something."
      return 'death'
    else
      text_buffer
      puts "I agree, but I wouldn't know where to start."

      return 'finished'
    end
  end
end

class Finished < Scene
  def enter()
    text_buffer
    puts "You won! Good job."
    text_buffer
  end
end


class Map
  @@scenes = {
    'central_corridor' => CentralCorridor.new(),
    'laser_weapon_armory' => LaserWeaponArmory.new(),
    'the_bridge' => TheBridge.new(),
    'escape_pod' => EscapePod.new(),
    'death' => Death.new(),
    'finished' => Finished.new(),
  }


  def initialize(start_scene)
    @start_scene = start_scene
  end


  def next_scene(scene_name)
    val = @@scenes[scene_name]
    return val
  end

  def opening_scene()
    return next_scene(@start_scene)
  end
end


a_map = Map.new('central_corridor')

a_game = Engine.new(a_map)

a_game.play()
