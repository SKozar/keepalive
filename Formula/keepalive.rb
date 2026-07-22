class Keepalive < Formula
  desc "Keep macOS awake for Teams during chosen hours"
  homepage "https://github.com/skozar/keepalive"
  version "0.3.0"
  url "https://github.com/skozar/keepalive/releases/download/v#{version}/keepalive"
  sha256 "e85d36f6540fbbc02f3d52275e92de18b6f05d69d1c92f0f24c7f15b9102a498"

  def install
    bin.install "keepalive"
  end

  def caveats
    <<~EOS
      To start the agent:
        keepalive start

      To run with custom schedule:
        keepalive start --schedule 04:00-12:00 --idle 180

      Logs: ~/Library/Logs/keepalive/keepalive.log

      IMPORTANT: Grant Accessibility permission to keepalive:
        System Settings → Privacy & Security → Accessibility
        Add: #{opt_bin}/keepalive
    EOS
  end
end
